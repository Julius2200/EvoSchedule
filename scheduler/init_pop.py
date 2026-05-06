import random

def initialize_pop(course_map, valid_rooms, assignments, room_cap_map, days, num_timeslots, num_chr):

    population = []

    for _ in range(0, num_chr):

        chromosome = []

        occupied_rooms = set()
        assigned_lecturers = set()
        assigned_levels = set()

        for course in course_map:
            c_index, level, duration, departments, class_size = course
            
            l_index = assignments[c_index]
            assigned = False
            retries = 50
            conflict = True
            day = None
            r_index = 0
            for rm in valid_rooms[c_index]:
                temp = None
                capacity = room_cap_map[rm]                    
                if capacity >= class_size:
                    r_index = rm
                    i_day = 0
                    i_time = 0
                    for i_day in range(4):
                        for i_time in range(10):
                            key = (rm, i_day, i_time)
                            if key in occupied_rooms:
                                continue
                elif temp == None:
                    temp = rm
                else:
                    rm_1 = room_cap_map[temp]
                    rm_2 = room_cap_map[rm]
                    if rm_1 < rm_2:
                        temp = rm_2
                    elif rm_1 == rm_2:
                        t_r = [rm_1, rm_2]
                        temp = random.choice(t_r)

            if duration > 1:
                time_1 = None
                time_2 = None
                while not assigned and conflict == True and retries > 0:
                    retries -= 1
                    day = random.randint(0, days - 1)
                    time_1 = random.randint(0, num_timeslots - 2)
                    time_2 = time_1 + 1
                    conflict = any ((level, dept, day, time_1) in assigned_levels for dept in departments)
                    lec_key_1 = (l_index, day, time_1)
                    lec_key_2 = (l_index, day, time_2)
                    if lec_key_1 in assigned_lecturers and lec_key_2 in assigned_lecturers:
                        conflict = True
                    else:
                        assigned_lecturers.add(lec_key_1)
                        assigned_lecturers.add(lec_key_2)
                    room_key_1 = (r_index, day, time_1)
                    room_key_2 = (r_index, day, time_2)
                    if room_key_1 in occupied_rooms and room_key_2 in occupied_rooms:
                        conflict = True
                    else:
                        occupied_rooms.add(room_key_1)
                        occupied_rooms.add(room_key_2)
                for dept in departments:
                    level_key_1 = (level, dept, day, time_1)
                    level_key_2 = (level, dept, day, time_2)
                    assigned_levels.add(level_key_1)
                    assigned_levels.add(level_key_2)

                
                assigned_lecturers.add(lec_key_1)
                assigned_lecturers.add(lec_key_2)

                room_key_1 = (r_index, day, time_1)
                room_key_2 = (r_index, day, time_2)
                occupied_rooms.add(room_key_1)
                occupied_rooms.add(room_key_2)
                gene_1 = (c_index, l_index, r_index, level, day, time_1)
                gene_2 = (c_index, l_index, r_index, level, day, time_2)
                chromosome.append(gene_1)
                chromosome.append(gene_2)
            else:
                time = None
                while not assigned and conflict == True and retries > 0:
                    retries -= 1
                    day = random.randint(0, days - 1)
                    time = random.randint(0, num_timeslots - 1)
                    conflict = any ((level, dept, day, time) in assigned_levels for dept in departments)
                    lec_key = (l_index, day, time)
                    if lec_key in assigned_lecturers:
                        conflict = True
                    else:
                        assigned_lecturers.add(lec_key)
                    room_key = (r_index, day, time)
                    if room_key in occupied_rooms:
                        conflict = True
                    else:
                        occupied_rooms.add(room_key)
                for dept in departments:
                    level_key = (level, dept, day, time)
                    assigned_levels.add(level_key)
                assigned_lecturers.add(lec_key)
                occupied_rooms.add(room_key)

                gene = (c_index, l_index, r_index, level, day, time)
                chromosome.append(gene)
        population.append(chromosome)

    return population