from utils.test_db import fetch_gen_data, get_assignment
#courses, lecturers, rooms = get_data()

max_gen = fetch_gen_data()
assignments = get_assignment()
#courses = []
#lecturers = []
#rooms = []
#assignments = {}

#def get_input_data():
#    return assignments

#def get_table_input():
#    return courses, lecturers, rooms

def get_day_data(data): 
    day = None
    match data:
        case 0:
            day = "Monday"
        case 1:
            day = "Tuesday"
        case 2:
            day = "Wednesday"
        case 3:
            day = "Thursday"
        case 4:
            day = "Friday"

        
    return day

def get_max_gen():
    return max_gen


def encode_assignment(assignment, courses, lecturers):
    course_index = {course["id"]: i for i, course in enumerate(courses)}
    lecturer_index = {lec["id"]: i for i, lec in enumerate(lecturers)}

    result = {}
    for id, lecturer in assignment.items():
        try:
            c_index = course_index[id]
            l_index = lecturer_index[lecturer]
        except KeyError as e:
            raise ValueError (f"Missing ID in data: {e}")
        result[c_index] = l_index

    return result
