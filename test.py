from algorithm.init_pop import initialize_population
from algorithm.timetable_builder import build_timetable
from algorithm.fitness import get_fitness
from algorithm.crossover import crossover
from algorithm.selection import tournament_selection
from algorithm.init_pop import initialize_population
from utils.test_db import get_table_details


courses, lecturers, rooms, assignments, departments, time_size, max_gen = get_table_details()
data = initialize_population(courses, lecturers, rooms, assignments, departments, time_size, max_gen)

#fitness_list = []
#for chromosome in data:
#    fitness = get_fitness(chromosome)
#    fitness_list.append(fitness)

#new_gen = tournament_selection(data, fitness_list, 3)

#for chromosome in data:
#    fitness, pen, s = get_fitness(chromosome)
#    print(f"{fitness}, penalty = {pen}, soft penalty = {s}\n")
"""c1, c2, p1, p2 = crossover(data[0], data[1])
items= []
items.append(c1)
items.append(c2)
items.append(p1)
items.append(p2)
i = 1
for item in items:
    table = build_timetable(item)
    print(f"table{i}\n\n")
    for gene in table:
        print(f"{gene.day} {gene.period}, {gene.course_id}, hosted by{gene.host_department}\n")
    i += 1"""

#temp = new_gen[0]
#table = build_timetable(temp)

#for gene in table:
#    print(f"{gene.day} {gene.period}, {gene.course_id}, by {gene.lecturer_name}, hosted by {gene.host_department}, for {gene.departments}, of {gene.level} at {gene.room_name} level\n")

#print(table)
