import random

def repair3(chromosome, fitness_dep, num_timeslots, days=5):
    repaired = []
    pending = []

    assigned_levels = set()
    assigned_lecturers = set()
    occupied_rooms = set()

    for gene in chromosome:
        c, l, r, level, d, t = gene
        departments, _ = fitness_dep[c]

        level_conflict = any((dept, level, d, t) in assigned_levels for dept in departments)
        lec_conflict = (l, d, t) in assigned_lecturers
        room_conflict = (r, d, t) in occupied_rooms

        if level_conflict or lec_conflict or room_conflict:
            pending.append(gene)
        else:
            repaired.append(gene)
            for dept in departments:
                assigned_levels.add((dept, level, d, t))
            assigned_lecturers.add((l, d, t))
            occupied_rooms.add((r, d, t))

    for gene in pending:
        c, l, r, level, _, _ = gene
        departments, _ = fitness_dep[c]
        retries = 0
        placed = False
        day = 0
        time = 0

        while retries < 100 and not placed:
            day = random.randint(0, days - 1)
            time = random.randint(0, num_timeslots - 1)

            level_conflict = any((dept, level, day, time) in assigned_levels for dept in departments)
            lec_conflict = (l, day, time) in assigned_lecturers
            room_conflict = (r, day, time) in occupied_rooms

            if not level_conflict and not lec_conflict and not room_conflict:
                placed = True
                break

            retries += 1

        if not placed:
            day = random.randint(0, days - 1)
            time = random.randint(0, num_timeslots - 1)

        for dept in departments:
            assigned_levels.add((dept, level, day, time))
        assigned_lecturers.add((l, day, time))
        occupied_rooms.add((r, day, time))
        repaired.append((c, l, r, level, day, time))

    return repaired