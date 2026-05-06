from algorithm.crossover import crossover
from algorithm.fitness import get_fitness
from algorithm.init_pop import initialize_population
from algorithm.mutation import block_mutate
from algorithm.selection import tournament_selection
from utils.helper import get_best
from algorithm.repair import repair
from utils.helper import build_course_room_map


def run_ga(courses, lecturers, rooms, assignments, departments, level_list, num_timeslots, max_gen, max_iter):
    course_room_map = build_course_room_map(courses, rooms)

    population = initialize_population(courses, lecturers, rooms, assignments, departments, level_list, num_timeslots, max_gen)
    generations = 1
    fitness_list = []

    for chromosome in population:
        fitness = get_fitness(chromosome, courses, lecturers, departments, rooms, level_list)
        fitness_list.append(fitness)

    
    best = get_best(fitness_list, population)
    s, c = best
    final_chromosome = ([], 0)
    found_best = False
    if s == 1:
        final_chromosome = (c, s)
        found_best = True
    else:
        found_best = False
    while not found_best and generations < max_iter:
        k = 3 if generations < 200 else 5

        selected = tournament_selection(population, fitness_list, k)
        next_gen = []
        for i in range(0, len(selected) - 1, 2):
            parent1 = selected[i]
            parent2 = selected[i+1]
            child1, child2 = crossover(parent1, parent2)
            next_gen.append(child1)
            next_gen.append(child2)

        new_gen = []
        for item in next_gen:
            mutation_entry = block_mutate(item, courses, course_room_map, assignments, departments, num_timeslots, mutation_rate=0.05)

            m_entry = repair(mutation_entry, courses, course_room_map, assignments, departments, 5, 10, 80)
            new_gen.append(m_entry)
        fit_list = []
        for chromosome in new_gen:
            fitness = get_fitness(chromosome, courses, lecturers, departments, rooms, level_list)
            fit_list.append(fitness)

        best = get_best(fit_list, new_gen)
        s, c = best
        if s == 1:
            final_chromosome = (c, s)
            found_best = True
            break
        else:
            found_best = False
            population = new_gen
            fitness_list = fit_list
            generations += 1

        print(f"best for gen {generations} = {s}")
        
        if generations == max_iter:
            best = get_best(fit_list, new_gen)
            s, c = best
            final_chromosome = (c, s)
            break

    return final_chromosome, generations