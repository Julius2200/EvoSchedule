from utils.data_loader import get_max_gen

def get_mutation_rate(generation):
    max_gens = get_max_gen()
    start = 0.2
    end = 0.05

    return start - (start - end) * (generation / max_gens)