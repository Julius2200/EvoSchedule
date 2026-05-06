

def encode_input_details(courses, lecturers, assignment_map, rooms):
    course_index_map = {item["course_id"]: i for i, item in enumerate(courses)}
    lecturer_index_map = {item["lecturer_name"]: i for i, item in enumerate(lecturers)}

    assignment = {}
    for key, value in assignment_map.items():
        if key in course_index_map and value in lecturer_index_map:
            assignment[course_index_map[key]] = lecturer_index_map[value]

    return assignment


