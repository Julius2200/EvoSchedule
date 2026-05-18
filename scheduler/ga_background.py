import threading
import time
import uuid
from datetime import datetime

from scheduler.ga_run import run_ga


def _now_iso():
    return datetime.utcnow().isoformat() + "Z"


def create_job(db, job_id, payload):
    doc = {
        "job_id": job_id,
        "status": "queued",
        "created_at": _now_iso(),
        **payload,
    }
    db.collection("ga_jobs").document(job_id).set(doc)


def update_job(db, job_id, payload):
    payload["updated_at"] = _now_iso()
    db.collection("ga_jobs").document(job_id).update(payload)


def run_ga_job(db, job_id, courses, lecturers, rooms, departments, assignment, global_settings, save_timetable_func):
    start = time.perf_counter()
    update_job(db, job_id, {"status": "running", "started_at": _now_iso()})

    try:
        decoded_timetable, best_fit = run_ga(
            courses,
            lecturers,
            rooms,
            departments,
            assignment,
            global_settings,
        )

        run_id = save_timetable_func(decoded_timetable)
        duration = round(time.perf_counter() - start, 4)

        update_job(db, job_id, {
            "status": "completed",
            "run_id": run_id,
            "fitness": best_fit,
            "duration": duration,
            "entries": len(decoded_timetable),
            "completed_at": _now_iso(),
        })
    except Exception as exc:
        duration = round(time.perf_counter() - start, 4)
        update_job(db, job_id, {
            "status": "failed",
            "error": str(exc),
            "duration": duration,
            "completed_at": _now_iso(),
        })


def start_ga_job_thread(db, courses, lecturers, rooms, departments, assignment, global_settings, save_timetable_func):
    job_id = str(uuid.uuid4())
    create_job(db, job_id, {"status": "queued"})
    thread = threading.Thread(
        target=run_ga_job,
        args=(db, job_id, courses, lecturers, rooms, departments, assignment, global_settings, save_timetable_func),
        daemon=True,
    )
    thread.start()
    return job_id
