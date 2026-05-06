import random

def repair(chromosome, courses, course_room_map, assignments, all_departments, num_of_days=5, num_timeslots=10, max_attempts=50):
    repaired = chromosome[:]

    used_lecturers = set()
    used_rooms = set()
    used_level_dept = set()

    for i in range(len(repaired)):
        c, l, r, d, t = repaired[i]

        course = courses[c]
        level = course["level"]
        departments = course["department"]
        dept_list  = []
        if "general" in departments:
            dept_list = all_departments
        else:
            dept_list = departments

        attempts = 0

        while attempts < max_attempts:
            conflict = False

            #----check lecturer----
            if (l,d,t) in used_lecturers:
                conflict = True

            #----check room----
            elif(r,d,t) in used_rooms:
                conflict = True

            #check level department
            elif any((level, dept, d, t) in used_level_dept for dept in dept_list):
                conflict = True

            if not conflict:
                used_lecturers.add((l, d, t))
                used_rooms.add((r, d, t))
                for dept in departments:
                    used_level_dept.add((level, dept, d, t))

                break

            d = random.randint(0, 4)
            t = random.randint(0, num_timeslots - 1)

            if random.random() < 0.3:
                r = random.choice(course_room_map[c])

            attempts += 1

            repaired[i] = (c, l, r, d, t)

            used_lecturers.add((l, d, t))
            used_rooms.add((r, d, t))
            for dept in departments:
                used_level_dept.add((level, dept, d, t))

    return repaired