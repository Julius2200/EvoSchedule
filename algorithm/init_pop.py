import random
from utils.helper import build_course_room_map

def get_class_size(level_list, keys, index):
    total = 0
    for item in keys:
        current_item = level_list[item]
        total += current_item[index]

    return total


def initialize_population(courses, lecturers, rooms, assignments, departments, level_list, num_timeslots, num_gens=10):
    course_room_map = build_course_room_map(courses, rooms)
    population =[]
    #create a room capacity map
    capacity_map = {}
    for i, room in enumerate(rooms):
        if i not in capacity_map:
            capacity_map[i] = room["capacity"]
    #repeat to prepare chromosomes for the number of generations
    for _ in range(num_gens):
        chromosome =[]
        assigned_lecturers = set()
        used_rooms = set()
        assigned_levels = set()
        assigned_double_period = set()

        #repeat for each course
        for c_index, course in enumerate(courses):
            frequency = course["frequency"]
            level = course["level"]
            depts = course["department"]
            dept_list = []
            class_size = 0#number of students taking the class

            if "general" in depts:
                class_size = get_class_size(level_list, departments, level)
                
            else:
                class_size = get_class_size(level_list, depts, level)
            lec_index = assignments[c_index]

            if frequency > 2:
                for _ in range(0, 2):
                    if c_index not in assigned_double_period:

                        assigned = False
                        attempts = 0
                        while not assigned and attempts < 100:
                            #room_index = random.choice(course_room_map[c_index])
                            room_gotten = False
                            #max_retries = len(rooms)
                            #retries = 0
                            #while not room_gotten:
                            #    room_index = random.choice(course_room_map[c_index])
                            #    if capacity_map[room_index] < class_size:
                            #        room_gotten = #True
                            #    elif(retries >= max_retries):
                            #        break
                            #    else:
                            #        retries += 1
                            room_index = None
                            for r_index in course_room_map[c_index]:
                                if capacity_map[r_index] >= (class_size * 0.75):
                                    room_index = r_index

                            day = random.randint(0, 4)
                            timeslot = random.randint(0, num_timeslots - 2)
                            second_time = 0
                            if timeslot == num_timeslots - 1:
                                second_time = timeslot - 1
                            else:
                                second_time = timeslot + 1
                            conflict = False
                            for _ in range(0):
                                lec_key_1 = (lec_index, day, timeslot)
                                lec_key_2 = (lec_index, day, second_time)
                                if (lec_key_1 not in assigned_lecturers) and (lec_key_2 not in assigned_lecturers):
                                    conflict = False
                                else:
                                    conflict = True
                            for _ in range(0):
                                room_key_1 = (room_index, day, timeslot)
                                room_key_2 = (room_index, day, second_time)
                                if (room_key_1 not in used_rooms) and (room_key_2 not in used_rooms):
                                    conflict = False
                                else:
                                    conflict = True

                            for _ in range(0):
                                conflict = any((level, dept, day, timeslot) in assigned_levels for dept in dept_list)
                                conflict = any((level, dept, day, second_time) in assigned_levels for dept in dept_list)

                            if conflict == False:
                                room_key_1 = (room_index, day, timeslot)
                                room_key_2 = (room_index, day, second_time)
                                lec_key_1 = (lec_index, day, timeslot)
                                lec_key_2 = (lec_index, day, second_time)
                                used_rooms.add(room_key_1)
                                used_rooms.add(room_key_2)
                                assigned_lecturers.add(lec_key_1)
                                assigned_lecturers.add(lec_key_2)
                                for dept in dept_list:
                                    level_key = (level, dept, day, timeslot)
                                    level_key_2 = (level, dept, day, second_time)
                                    assigned_levels.add(level_key)
                                    assigned_levels.add(level_key_2)
                                assigned_double_period.add(c_index)
                                gene = (c_index, lec_index, room_index, day, timeslot)
                                gene_2 = (c_index, lec_index, room_index, day, second_time)
                                chromosome.append(gene)
                                chromosome.append(gene_2)
                                assigned = True
                            else:
                                attempts += 1
                    else:
                        attempts = 0
                        assigned = False
                        while not assigned and attempts < 100:
                            #room_index = random.choice(course_room_map[c_index])
                            #room_gotten = False
                            #max_retries = len(rooms)
                            #retries = 0
                            #while not room_gotten:
                            #    room_index = random.choice(course_room_map[c_index])
                            #    if capacity_map[room_index] < class_size:
                            #        room_gotten = True
                            #    elif retries >= max_retries:
                            #        break
                            #    else:
                            #        retries += 1

                            room_index = None
                            for r_index in course_room_map[c_index]:
                                if capacity_map[r_index] >= (class_size * 0.75):
                                    room_index = r_index

                            day = random.randint(0, 4)
                            timeslot = random.randint(0, num_timeslots - 1)
                            conflict = False
                            conflict = any((level, dept, day, timeslot) in assigned_levels for dept in dept_list)
                            lec_key = (lec_index, day, timeslot)
                            room_key = (room_index, day, timeslot)
                            if lec_key in assigned_lecturers:
                                conflict = True
                            if room_key in used_rooms:
                                conflict = True
                            if conflict == False:
                                gene = (c_index, lec_index, room_index, day, timeslot)
                                chromosome.append(gene)
                                used_rooms.add(room_key)
                                assigned_lecturers.add(lec_key)
                                for dept in dept_list:
                                    level_key = (level, dept, day, timeslot)
                                    assigned_levels.add(level_key)
                                assigned = True
                            else:
                                attempts += 1

                            gene = (c_index, lec_index, room_index, day, timeslot)
                            chromosome.append(gene)
                            used_rooms.add(room_key)
                            assigned_lecturers.add(lec_key)
                            for dept in dept_list:
                                level_key = (level, dept, day, timeslot)
                                assigned_levels.add(level_key)
                        
            else:
                for _ in range(0, frequency):
                    assigned = False
                    attempts = 0
                    while not assigned and attempts < 100:
                        #room_index = random.choice(course_room_map[c_index])
                        #room_gotten = False
                        #max_retries = len(rooms)
                        #retries = 0
                        #while not room_gotten:
                        #    room_index = random.choice(course_room_map[c_index])
                        #    if capacity_map[room_index] < class_size:
                        #        room_gotten = True
                        #    elif retries >= max_retries:
                        #        break
                        #    else:
                        #        retries += 1

                        room_index = None
                        for r_index in course_room_map[c_index]:
                            if capacity_map[r_index] >= (class_size * 0.75):
                                room_index = r_index

                        day = random.randint(0, 4)
                        timeslot = random.randint(0, num_timeslots - 1)
                        room_key = (room_index, day, timeslot)
                        lec_key = (lec_index, day, timeslot)
                        conflict = any((level, dept, day, timeslot) in assigned_levels for dept in dept_list)
                        if room_key in used_rooms:
                            conflict = True
                        if lec_key in assigned_lecturers:
                            conflict = True

                        if conflict == False:
                            used_rooms.add(room_key)
                            assigned_lecturers.add(lec_key)
                            for dept in dept_list:
                                level_key = (level, dept, day, timeslot)
                                assigned_levels.add(level_key)

                            gene = (c_index, lec_index, room_index, day, timeslot)
                            chromosome.append(gene)
                            assigned = True
                        else:
                            attempts += 1

                        gene = (c_index, lec_index, room_index, day, timeslot)
                        chromosome.append(gene)
                        used_rooms.add(room_key)
                        assigned_lecturers.add(lec_key)
                        for dept in dept_list:
                            level_key = (level, dept, day, timeslot)
                            assigned_levels.add(level_key)
                        assigned = True
        
        population.append(chromosome)

    return population