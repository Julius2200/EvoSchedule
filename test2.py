from data_mgt.data_loader import *
from scheduler.init_pop import initialize_pop
from scheduler.fitness import fitness
from scheduler.selection import selection
from utils.test_db import get_table_details, get_num_timeslots, get_days, get_mid_day
from utils.test_db import get_level_list

courses, lecturers, rooms, assignments, departments, time_size, max_gen, max_iter = get_table_details()

level_list = get_level_list()

num_timeslots = get_num_timeslots()
days = get_days()
mid_day = get_mid_day()

course_map = create_course_schedule(courses, level_list)

valid_rooms = valid_rooms(rooms, courses)

room_cap_map = get_room_cap_map(rooms)

fitness_dep = get_fitness_dep(courses, level_list)
lec_tod_map = get_lec_tod_map(lecturers)
lec_workload_map = get_lec_workload_map(lecturers)

population = initialize_pop(course_map, valid_rooms, assignments, room_cap_map, days, num_timeslots, max_gen)

#print(population)
print(len(population))
print(len(population[0]))

print("fitness section")

num_lecturers = len(lecturers)
i = 0

#for j in range(len(population)):
#    fitness = fitness(population[j], fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers)

#   print(f"chromosome {i} : fitness : {fitness}")
#    i += 1

#fitness = fitness(population[0], fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers)
#print(fitness)

fitness_list = []

length_needed = len(population)
while i < length_needed:
    fit = fitness(population[i], fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers)

    fitness_list.append(fit)

    print(f"Chromosome {i} fitness: {fit}")

    i += 1

new_gen = selection(population, fitness_list, days, room_cap_map, fitness_dep, num_timeslots, 1, 3, 2, 0.3)

m = 0
while m < len(new_gen):
    f = fitness(new_gen[m], fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers)

    print(f"Chromosome {m} fitness: {f}")

    m += 1

#print(f"{new_gen[0]}")