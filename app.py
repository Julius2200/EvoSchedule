import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
import json
import os
import uuid
from firebase_admin import credentials, firestore
from scheduler.ga_run import run_ga
from scheduler.ga_background import start_ga_job_thread
from data_mgt.data_loader import get_periods
from utils.date_generator import generate_run_id

app = Flask(__name__)
CORS(app)#enable CORS for all routes

# initialize firebase admin SDK from secure env var or local key.json fallback
firebase_service_account = os.environ.get("FIREBASE_SERVICE_ACCOUNT_JSON")
if firebase_service_account:
    try:
        service_account_info = json.loads(firebase_service_account)
        cred = credentials.Certificate(service_account_info)
    except json.JSONDecodeError as exc:
        raise ValueError("FIREBASE_SERVICE_ACCOUNT_JSON contains invalid JSON") from exc
elif os.path.exists("key.json"):
    cred = credentials.Certificate("key.json")
else:
    raise EnvironmentError(
        "Firebase credentials not found. Set FIREBASE_SERVICE_ACCOUNT_JSON or provide key.json."
    )

firebase_admin.initialize_app(cred)

#initialize firestore
db = firestore.client()

#----- data writing function -----
def resolve_document_id(collection_name, item):
    """Resolve a stable document id for the incoming item.
    If the item provides a natural unique key, use it so newer entries override old ones.
    """
    # Ensure item is a dictionary
    if not isinstance(item, dict):
        raise ValueError(f"Expected dict for {collection_name}, got {type(item).__name__}")

    natural_keys = {
        "courses": ["id"],
        "lecturers": ["id"],
        "rooms": ["id"],
        "departments": ["id"]
    }

    for key in natural_keys.get(collection_name, []):
        if item.get(key) is not None:
            return str(item[key])

    return str(uuid.uuid4())


def write_dataset(collection_name, data_list):
    """
    Writes ONLY one dataset at a time to firestore (top-level collections). Uses batch writes with max 500 operations.
    Incoming items with the same resolved ID override prior entries.
    """
    if not isinstance(data_list, list):
        raise ValueError(f"Expected list for {collection_name}, got {type(data_list).__name__}")

    # Deduplicate incoming data by resolved document ID, keeping later entries.
    deduped = {}
    for idx, item in enumerate(data_list):
        try:
            doc_id = resolve_document_id(collection_name, item)
            item["id"] = doc_id
            deduped[doc_id] = item
        except Exception as e:
            raise ValueError(f"Error processing item {idx} in {collection_name}: {str(e)}")

    batch = db.batch()
    operation_count = 0
    collection_ref = db.collection(collection_name)

    for doc_id, item in deduped.items():
        doc_ref = collection_ref.document(doc_id)
        batch.set(doc_ref, item)
        operation_count += 1

        if operation_count == 500:
            batch.commit()
            batch = db.batch()
            operation_count = 0

    if operation_count > 0:
        batch.commit()

    print(f"{collection_name} written successfully ({len(deduped)} items)")

#Single write function
def write_single_document(collection_name, document_name, data):
    doc_ref = db.collection(collection_name).document(document_name)
    doc_ref.set(data)

def normalize_assignment_data(data):
    """Normalize assignment payloads into a dict mapping id to lecturer name."""
    if isinstance(data, dict):
        return data

    if isinstance(data, list):
        if all(isinstance(item, dict) and len(item) == 1 for item in data):
            merged = {}
            for item in data:
                merged.update(item)
            return merged

        if all(isinstance(item, dict) and "id" in item and "name" in item for item in data):
            return {item["id"]: item["name"] for item in data}

        if all(isinstance(item, (list, tuple)) and len(item) == 2 for item in data):
            return dict(data)

    raise ValueError("Assignment data must be a dict or list of key/value pairs.")

#store assignments
def store_assignment(data):
    normalized = normalize_assignment_data(data)
    write_single_document("config", "assignment", normalized)

#store global settings
def store_global_settings(data):
    write_single_document("config", "global_settings", data)

#write level data
def store_level_data(data):
    write_single_document("config", "level_data", data)


#load config data for GA
def load_config():
    config_ref = db.collection("config")

    assignment = config_ref.document("assignment").get().to_dict()
    global_settings = config_ref.document("global_settings").get().to_dict()
    levels = config_ref.document("level_data").get().to_dict()

    if assignment is None:
        assignment = {}
    elif not isinstance(assignment, dict):
        assignment = normalize_assignment_data(assignment)

    return assignment, global_settings, levels

#save timetable batch + date as id
def save_timetable(timetable):
    run_id = generate_run_id()

    batch = db.batch()
    operation_count = 0

    for i, entry in enumerate(timetable):
        doc_id = f"{run_id}_{i}"

        # Convert Timetable_entry object to dict if needed
        if isinstance(entry, dict):
            entry_dict = entry
        elif hasattr(entry, "__dict__"):
            entry_dict = entry.__dict__
        else:
            entry_dict = {"data": str(entry)}

        doc_ref = db.collection("timetables").document(doc_id)
        batch.set(doc_ref, {
            **entry_dict,
            "run_id": run_id
        })
        operation_count += 1
        if operation_count == 500:
            batch.commit()
            batch = db.batch()
            operation_count = 0
    if operation_count > 0:
        batch.commit()

    return run_id

#fetch all collection
def load_collection(collection_name):
    docs = db.collection(collection_name).stream()
    data = []
    for doc in docs:
        item = doc.to_dict()
        item["id"] = doc.id
        data.append(item)

    return data

#load all required GA data
def load_ga_data():
    departments = load_collection("departments")
    return{
        "courses": load_collection("courses"),
        "lecturers": load_collection("lecturers"),
        "rooms": load_collection("rooms"),
        "departments": [dept.get("id") for dept in departments]
    }

@app.route('/departments', methods=['GET'])
def get_departments():
    try:
        data = load_collection('departments')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        data = load_collection('courses')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/rooms', methods=['GET'])
def get_rooms():
    try:
        data = load_collection('rooms')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/lecturers', methods=['GET'])
def get_lecturers():
    try:
        data = load_collection('lecturers')
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/assignments', methods=['GET'])
def get_assignments():
    try:
        assignment, _, _ = load_config()
        return jsonify(assignment), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/global_settings', methods=['GET', 'POST'])
def global_settings():
    if request.method == 'GET':
        try:
            _, global_settings, _ = load_config()
            return jsonify(global_settings), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    try:
        data = request.get_json()
        store_global_settings(data)
        return jsonify({"message": "Global settings stored"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#------- api endpoints ----------
@app.route('/save_departments', methods=["POST"])
def save_departments():
    data = request.get_json()
    write_dataset("departments", data)
    return jsonify({"message": "Departments saved"}), 200

@app.route('/save_lecturers', methods=["POST"])
def save_lecturers():
    data = request.get_json()
    write_dataset("lecturers", data)
    return jsonify({"message": "Lecturers saved"}), 200

@app.route('/save_courses', methods=["POST"])
def save_courses():
    data = request.get_json()
    write_dataset("courses", data)
    return jsonify({"message": "Courses saved"}), 200

@app.route('/save_rooms', methods=["POST"])
def save_rooms():
    data = request.get_json()
    write_dataset("rooms", data)
    return jsonify({"message": "Rooms saved"}), 200

@app.route('/save_assignments', methods=["POST"])
def save_assignments():
    try:
        data = request.get_json()
        store_assignment(data)
        return jsonify({"message": "Assignment stored"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#@app.route('/global_settings', methods=["POST"])
#def global_settings():
#    try:
#        data = request.get_json()
#        store_global_settings(data)
#        return jsonify({"message": "Global settings stored"}), 200
#    except Exception as e:
#        return jsonify({"error": str(e)}), 500
    
@app.route('/levels', methods=["POST"])
def save_levels():
    try:
        data = request.get_json()
        store_level_data(data)
        return jsonify({"message": "Level data saved"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/run_ga', methods=["POST"])
def run_gen_algo():
    try:
        # Load config
        assignment, global_settings, levels = load_config()
        ga_data = load_ga_data()

        courses = ga_data["courses"]
        lecturers = ga_data["lecturers"]
        rooms = ga_data["rooms"]
        departments = ga_data["departments"]
        adj_assignment = assignment

        job_id = start_ga_job_thread(
            db,
            courses,
            lecturers,
            rooms,
            departments,
            adj_assignment,
            global_settings,
            save_timetable,
        )

        return jsonify({
            "message": "GA job started",
            "job_id": job_id,
            "status_url": f"/run_ga_status/{job_id}",
        }), 202
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/run_ga_status/<job_id>', methods=["GET"])
def get_run_ga_status(job_id):
    try:
        job_doc = db.collection("ga_jobs").document(job_id).get()
        if not job_doc.exists:
            return jsonify({"error": "Job not found"}), 404

        job_data = job_doc.to_dict()
        job_data["job_id"] = job_id
        return jsonify(job_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
#fetch timetable
@app.route('/get_timetable/<run_id>', methods=["GET"])
def get_timetable(run_id):
    try:
        docs = db.collection("timetables")\
        .where("run_id", "==", run_id)\
        .stream()
        result = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            result.append(data)

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "Hello world!!!"

@app.route('/login', methods=["POST"])
def admin_login():
    data = request.get_json()

if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host="0.0.0.0",
        port = port
    )