import random

def get_elites(population, fitness_scores, num_elites=3):
    #pair individuals with scores and sort by fitness (descending)
    paired = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
    #extract just the individuals for the top n slots
    elites = [ind for ind, score in paired[:num_elites]]
    return elites


def tournament_selection(population, fitness_scores, k=4):
    new_gen = get_elites(population, fitness_scores, 5)
    while len(new_gen) < len(population):
        selected_indices = random.sample(range(len(population)), k)
        #identify the index with the maximum fitness in that sample
        best_index = max(selected_indices, key=lambda i: fitness_scores[i])
        new_gen.append(population[best_index])

    #return the winner
    return new_gen
