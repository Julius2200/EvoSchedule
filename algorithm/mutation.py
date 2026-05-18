import random

def group_blocks(chromosome):
    blocks = []
    visited = set()

    for i, gene in enumerate(chromosome):
        if i in visited:
            continue

        c, l, r, d, t = gene
        block = [i]

        #check for consecutive same-course slots (double period)
        for j in range(i+1, len(chromosome)):
            c2, l2, r2, d2, t2 = chromosome[j]
            if c2 == c and d2 == d and abs(t2 - t) == 1:
                block.append(j)
                visited.add(j)
        visited.add(i)
        blocks.append(block)
    return blocks

def block_mutate(chromosome, courses, course_room_map,assignments, departments, num_timeslots, mutation_rate):
    new_chromosome = chromosome[:]
    blocks = group_blocks(chromosome)

    #build used sets
    assigned_lecturers = set()
    used_rooms = set()
    assigned_level = set()

    for (c, l, r, d, t) in chromosome:
        level = courses[c]["level"]
        for dept in courses[c]["department"]:
            if "general" in dept:
                dept = departments
            assigned_level.add((level, dept, d, t) for dept in dept)
            assigned_lecturers.add((l, d, t))
            used_rooms.add((r, d, t))

    for block in blocks:
        if random.random() > mutation_rate:
            continue
        genes = [new_chromosome[i] for i in block]
        c = genes[0][0]
        level = courses[c]["level"]
        department = courses[c]["department"]
        if "general" in department:
            department = departments
        
        #remove old
        for (_, l, r, d, t) in genes:
            assigned_lecturers.discard((l, d, t))
            used_rooms.discard((r, d, t))
            for dept in department:
                assigned_level.discard((level, dept, d, t))
        period_len = len(block)

        #try new placement
        for _ in range(20):
            new_l = assignments[c]
            new_r = random.choice(course_room_map[c])
            new_d = random.randint(0, 4)
            new_t = random.randint(0, num_timeslots - period_len)

            conflict = False
            for dt in range(period_len):
                if (new_l, new_d, new_t+dt) in assigned_lecturers:
                    conflict = True
                    break
                if (new_r, new_d, new_t+dt) in used_rooms:
                    conflict = True
                    break
                if any((level, dept, new_d, new_t+dt) in assigned_level for dept in department):
                    conflict = True
                    break
            if not conflict:
                #apply
                for idx, dt in zip(block, range(period_len)):
                    new_chromosome[idx] = (c, new_l, new_r, new_d, new_t+dt)
                    assigned_lecturers.add((new_l, new_d, new_t+dt))
                    used_rooms.add((new_r, new_d, new_t+dt))
                    for dept in department:
                        assigned_lecturers.add((level, dept, new_d, new_t+dt))
                break

    return new_chromosome
