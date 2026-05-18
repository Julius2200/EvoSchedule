import random

def crossover(parent1, parent2):
    slice_point = random.randint(1, len(parent1) - 2)
    child1 = parent1[ :slice_point] + parent2[slice_point: ]
    child2 = parent2[ :slice_point] + parent1[slice_point: ]

    return child1, child2
