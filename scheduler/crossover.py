import random

def get_safe_boundaries(chromosome):
    """Return indices where it is safe to cut. Excludes the indices between a double period"""
    safe_indices = [] #It is always safe to cut at the start
    i = 0
    safe_indices.append(i)
    while i < len(chromosome) - 1:
        t1 = chromosome[i]
        t2 = chromosome[i + 1]

        #check if they are double period
        is_double = (t1[:5] == t2[:5] and t2[5] == t1[5] + 1)

        if is_double:
            #skip the index between them and move to after the pair
            i += 2
            safe_indices.append(i)
        else:
            #if single the very next index is a safe boundary
            i += 1
            safe_indices.append(i)
    #ensure the end of the chromosome is included if not already
    if len(chromosome) not in safe_indices:
        safe_indices.append(len(chromosome))

    return safe_indices

def two_point_crossover(parent1, parent2):
    boundaries_1 = get_safe_boundaries(parent1)
    boundaries_2 = get_safe_boundaries(parent2)
    if len(boundaries_1) < 2:
        return parent1[:], parent2[:]#Not enough cut points

    pt1, pt2 = sorted(random.sample(boundaries_1, 2))
    pt3, pt4 = sorted(random.sample(boundaries_2, 2))

    child1 = parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]
    child2 = parent2[:pt3] + parent1[pt3:pt4] + parent2[pt4:]

    return child1, child2
