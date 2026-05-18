
def get_tod(data, mid_day):
    value = 0
    if data < mid_day:
        value = 0
    else:
        value = 1
    return value

def fitness(chromosome, fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers):
    h_penalty = 0
    s_penalty = 0
    assigned_lecturers = set()
    occupied_rooms = set()
    assigned_levels = set()

    for gene in chromosome:
        c_index, l_index, r_index, level, day, timeslot = gene
        departments, class_size = fitness_dep[c_index]
        capacity = room_cap_map[r_index]

        #Hard constraints
        #level double-booking per department and level
        level_conflict = any((dept, level, day, timeslot) in assigned_levels for dept in departments)
        if level_conflict:
            h_penalty += 1
        else:
            for dept in departments:
                assigned_levels.add((dept, level, day, timeslot))

        #lecturer double booking
        lec_key = (l_index, day, timeslot)
        if lec_key in assigned_lecturers:
            h_penalty += 1
        else:
            assigned_lecturers.add(lec_key)

        #room double-booking
        room_key = (r_index, day, timeslot)
        if room_key in occupied_rooms:
            h_penalty += 1
        else:
            occupied_rooms.add(room_key)

        #soft_constraints
        #room capacity
        if capacity <= (class_size * 0.75):
            s_penalty += 3
        elif capacity < class_size:
            s_penalty += 2

        #lecturer time of day
        tod = get_tod(timeslot, mid_day)
        l_tod = lec_tod_map[l_index]
        if tod != l_tod:
            s_penalty += 2

    for i in range(num_lecturers):
        lec_index = i
        workload = lec_workload_map[lec_index] * 5
        count = 0

        for gene in chromosome:
            c, l, r, lvl, d, t = gene
            
            if l == lec_index:
                count += 1

        if workload < count:
            s_penalty += 1
    hard_penalty = h_penalty * 10  # Reduced from 20 to 5 for faster convergence
    penalty = hard_penalty + s_penalty

    fitness = 1/(1 + penalty)

    return fitness
