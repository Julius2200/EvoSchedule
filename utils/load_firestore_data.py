from database.firebase_config import init_firestore
from utils.data_loader import fetch_collection
from utils.format_data import format_data

def load_data_from_firestore():
    db = init_firestore()

    #fetch collections
    courses = fetch_collection(db, "courses")
    rooms = fetch_collection(db, "rooms")
    lecturers = fetch_collection(db, "lecturers")
    timeslots = fetch_collection(db, "timeslots")

    config_doc = db.collection("config").document("general").get()
    config = config_doc.to_dict()
    num_days = config["num_days"]

    #format data
    courses, rooms, lecturers, timeslots = format_data(courses, rooms, lecturers, timeslots)

    return courses, rooms, lecturers, timeslots, num_days