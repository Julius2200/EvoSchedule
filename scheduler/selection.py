import random
from scheduler.crossover import two_point_crossover
from scheduler.mutation import mutate
from scheduler.repair import repair3

def selection(chromosomes, fitness, day, room_cap_map, fitness_dep, num_timeslots, gens, k, elites_count, mutation_rate, assignments=None, valid_rooms=None):
    #initialize a new generation
    new_gen = []

    #combine chromosome and fitness using the zip function
    combined = sorted(zip(fitness, chromosomes), key=lambda x: x[0], reverse=True)

    sorted_chromosomes = [chromo for fitness, chromo in combined]

    #elitism
    for i in range(elites_count):
        elite = sorted_chromosomes[i]
        new_gen.append(elite)

    #Tournament selection
    length = max(len(chromosomes), 100)
    while len(new_gen) < length:
        indices = random.sample(range(len(chromosomes)), k)

        index1 = max(indices, key=lambda idx: fitness[idx])
        parent1 = chromosomes[index1]

        indices2 = random.sample(range(len(chromosomes)), k)

        index2 = max(indices2, key=lambda idx: fitness[idx])
        parent2 = chromosomes[index2]

        ch1, ch2 = two_point_crossover(parent1, parent2)

        if gens > 0:
            child1, child2 = mutate(ch1, ch2, day, mutation_rate, assignments, valid_rooms)
        else:
            child1, child2 = ch1, ch2

        repaired = repair3(child1, fitness_dep, num_timeslots)
        repaired2 = repair3(child2, fitness_dep, num_timeslots)

        new_gen.append(repaired)
        if len(new_gen) < length:
            new_gen.append(repaired2)
            
    return new_gen
