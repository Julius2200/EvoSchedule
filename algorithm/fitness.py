from utils.helper import get_tod_map
from utils.helper import get_tod
"""
---hard constraints---
1. no lecturer double booking
2. no room double booking
3. no level double booking

---soft constraints---
1. lecturer workload
2. time of day preference
"""

def get_class_size(levels, keys, index):
    total = 0
    for item in keys:
        current_item = levels[item]
        total += current_item[index]

    return total


def calc_lec_workload(chromosome, lecturers):
    mapping = {i : 0 for i, lec in enumerate(lecturers)}
    for gene in list(chromosome):
        c, l, _, _, _ = gene
        if l not in mapping:
            mapping[l] = 0
        mapping[l] += 1
    return mapping


def get_fitness(chromosome, courses, lecturers, departments, rooms, level_list):
    penalty = 0
    soft_penalty = 0

    used_rooms = set()
    used_lecturers = set()
    used_levels = set()
    lec_workload_map = calc_lec_workload(chromosome, lecturers)

    lec_tod_map = get_tod_map(lecturers)
    
    #create a room capacity map
    capacity_map = {}
    for i, room in enumerate(rooms):
        if i not in capacity_map:
            capacity_map[i] = room["capacity"]

    for gene in chromosome:

        c_indx, l_indx, r_indx, day, timeslot = gene
        
        present_course = courses[c_indx]
        level = present_course["level"]
        depts = present_course["department"]
        dept_list = []
        if "general" in depts:
            dept_list = departments
        else:
            dept_list = depts

        #---hard constraints---
        #lecturer double-booking
        lec_key = (l_indx, day, timeslot)
        if lec_key not in used_lecturers:
            used_lecturers.add(lec_key)
        else:
            penalty += 1

        #room double booking
        room_key = (r_indx, day, timeslot)
        if room_key not in used_rooms:
            used_rooms.add(room_key)
        else:
            penalty += 1

        
        current_course = courses[c_indx]
        lvl = current_course["level"]

        #level double-booking
        if any((lvl, dept, day, timeslot) not in used_levels for dept in dept_list):
            for dept in dept_list:
                level_entry = (lvl, dept, day, timeslot)
                used_levels.add(level_entry)
        else:
            penalty += 1

        #room capacity check
        class_size = 0#number of students taking the class

        class_size = get_class_size(level_list, dept_list, level)
        if capacity_map[r_indx] < (class_size * 0.7):
            #soft_penalty += 1
            pass
                

        #---soft constraints---
        #lec tod check
        l_tod = lec_tod_map[l_indx]
        tod_check = get_tod(timeslot)

        if l_tod != tod_check:
            soft_penalty += 1

    #lec workload check
    for i, lec in enumerate(lecturers):

        workload_value = lec["workload"] * 5
        workload_check = lec_workload_map[i]
        if workload_check > workload_value:
            soft_penalty += 1


    total = (penalty * 10) + soft_penalty
    score = ((1)/(1 + total))
    fitness = round(score, 4)

    return fitness