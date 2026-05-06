def get_best(fit, pop):
    best_fitness, best_chromosome = max(zip(fit, pop))

    return best_fitness, best_chromosome


def classify_course(courses):
    course_category = []

    for course in courses:
        if course["department"] == "general":
            course_category.append("GENERAL")
        elif len(course["department"]) > 1:
            course_category.append("SHARED")
        else:
            course_category.append("ISOLATED")

    return course_category

def build_course_room_map(courses, rooms):
    mapping = {}

    categories = classify_course(courses)
    for i, course in enumerate(courses):
        preferred = []
        fallback = []
        category = categories[i]

        for j, room in enumerate(rooms):
            if category == "GENERAL":
                if room["is_shared"]:
                    preferred.append(j)
            else:
                if room["department"] == course["host_department"]:
                    preferred.append(j)
                elif room["is_shared"]:
                    fallback.append(j)

        mapping[i] = preferred + fallback

    return mapping

def get_tod_map(lecturers):
    l_map = {}
    for l_index, lec in enumerate(lecturers):
        l_map[l_index] = lec["tod"]

    return l_map

def get_tod(data):
    value = None
    match data:
        case 0|1|2|3:
            value = 0
        
        case 4|5|6|7|8|9|10:
            value = 1

    return value

