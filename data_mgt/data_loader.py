def create_course_schedule(courses, level_list, dept_list):
    result = []
    for i, course in enumerate(courses):
        level = course["level"]
        freq = course["frequency"]
        dept = course["department"]
        if "general" in dept:
            dept = dept_list
        size = 0

        for d in dept:
            entry = level_list[d]
            size += entry[level]
        if freq > 2:
            entry_1 = (i, level, 2, dept, size)
            entry_2 = (i, level, 1, dept, size)

            result.append(entry_1)
            result.append(entry_2)

        elif freq == 2:
            entry_1 = (i, level, 1, dept, size)
            entry_2 = (i, level, 1, dept, size)
            result.append(entry_1)
            result.append(entry_2)

        else:
            entry = (i, level, 1, dept, size)
            result.append(entry)

    return result


def valid_rooms(rooms, courses):
    course_room_map = {}

    for i, course in enumerate(courses):
        priority = []
        fallback = []
        for j, room in enumerate(rooms):
            host = course["host_department"]
            if room["department"] == host:
                priority.append(j)
            elif room["department"] == None:
                fallback.append(j)
            else:
                continue
        options = (priority + fallback)
        course_room_map[i] = options
    return course_room_map

def get_room_cap_map(rooms):
    room_cap_map = {}

    for  i, room in enumerate(rooms):
        capacity = room["capacity"]
        room_cap_map[i] = capacity

    return room_cap_map

def get_fitness_dep(courses, level_list, dept_list):
    result = {}

    for i, course in enumerate(courses):
        dept = course["department"]
        if "general" in dept:
            dept = dept_list
        level = course["level"]

        class_size = 0
        count = 0
        for d in dept:
            entry = level_list[d]
            count += entry[level]

        class_size = count

        dep_entry = (dept, class_size)

        result[i] = dep_entry
    return result

def get_lec_workload_map(lecturers):
    result = {}
    for l, lec in enumerate(lecturers):
        workload = lec["workload"]
        result[l] = workload

    return result

def get_lec_tod_map(lecturers):
    result = {}
    for l, lec in enumerate(lecturers):
        tod = lec["tod"]
        result[l] = tod
    
    return result

def get_mid_day(start_hour):
    i = -1
    x = start_hour
    while x <= 12:
        i += 1
        x += 1
    return i

def get_periods(start_hour, stop_hour):
    periods = []
    for hour in range(start_hour, stop_hour):
        start = f"{hour :02d}:00"
        stop = f"{hour +1 :02d}:00"
        periods.append(f"{start} - {stop}")

    return periods