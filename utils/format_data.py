

def format_data(courses, rooms, lecturers, timeslots):
    #Map course id -> index
    course_index_map = {
        c["id"]: i for i, c in enumerate(courses)
    }

    #format lecturers (convert ids -> indexes)
    formatted_lecturers = []
    for lec in lecturers:
        formatted_lecturers.append({
            "name":lec["name"],
            "courses": [course_index_map[cid] for cid in lec["courses"] if cid in course_index_map]
        })

    #format timeslots (just labels)
    formatted_timeslots = [t["label"] for t in timeslots]

    return courses, rooms, formatted_lecturers, formatted_timeslots
