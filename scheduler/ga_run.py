from scheduler.init_pop import initialize_pop
from scheduler.models import *
from scheduler.fitness import fitness
from scheduler.repair import repair3
from scheduler.selection import selection
from scheduler.timetable_builder import build_timetable
from data_mgt.codec import encode_input_details
from data_mgt.data_loader import *


def get_best_chromosome(chromosomes, fitness):
    combined = sorted(zip(chromosomes, fitness), key=lambda x: x[1], reverse=True)

    sorted_chromosomes = [chromo for chromo, fit in combined]
    sorted_fitness = [fit for chromo, fit in combined]

    result = sorted_chromosomes[0]
    fit = sorted_fitness[0]
    return result, fit


def normalize_global_settings_level_list(global_settings):
    """Convert nested level_list keys to int so the GA can index by level."""
    if not isinstance(global_settings, dict):
        return

    level_list = global_settings.get("level_list")
    if not isinstance(level_list, dict):
        return

    normalized = {}
    for dept, levels in level_list.items():
        if isinstance(levels, dict):
            normalized[dept] = {int(k): v for k, v in levels.items()}
        else:
            normalized[dept] = levels

    global_settings["level_list"] = normalized


def run_ga(courses, lecturers, rooms, departments, assignment, global_settings):
    max_chrom = 200  # Increased population size for better exploration
    max_gen = 500
    stagnation_limit = 50  # Stop if no improvement for 50 generations

    valid_room = valid_rooms(rooms, courses)
    assignments = encode_input_details(courses, lecturers, assignment, rooms)
    normalize_global_settings_level_list(global_settings)
    timeslot_data = global_settings["timeslot_data"]
    start_hour = timeslot_data["start_hour"]
    stop_hour = timeslot_data["stop_hour"]
    num_timeslots = stop_hour - start_hour
    level_list = global_settings["level_list"]
    days = global_settings["days"]
    mid_day = get_mid_day(start_hour)
    num_lecturers = len(lecturers)


    course_map = create_course_schedule(courses, level_list, departments)
    


    room_cap_map = get_room_cap_map(rooms)

    fitness_dep = get_fitness_dep(courses, level_list, departments)
    lec_tod_map = get_lec_tod_map(lecturers)
    lec_workload_map = get_lec_workload_map(lecturers)

    attempts = 0

    population = initialize_pop(course_map, valid_room, assignments, room_cap_map, days, num_timeslots, max_chrom)
    population = [repair3(chrom, fitness_dep, num_timeslots) for chrom in population]

    fitness_list = []
    for chromosome in population:
        fit = fitness(chromosome, fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers)
        
        fitness_list.append(fit)

    best_solution, best_fit = get_best_chromosome(population, fitness_list)

    final_chromosome = list()
    final_fitness = None

    # Track best fitness for stagnation detection
    best_fitness_history = [best_fit]
    stagnation_counter = 0

    found = False
    new_gen = []
    fit_list = []
    while not found and attempts <= max_gen:
        fit_list = []
        new_gen = []
        # Adaptive parameters based on generation and stagnation
        progress_ratio = attempts / max_gen
        diversity_factor = len(set(tuple(chromo) for chromo in population)) / len(population)
        
        if stagnation_counter > 10:
            # Increase exploration when stagnated
            k = 5
            e = max(1, int(2 * (1 - progress_ratio)))
            m = min(0.6, 0.2 + stagnation_counter * 0.01)
        elif progress_ratio < 0.3:
            # Early generations: exploration
            k = 3
            e = 2
            m = 0.4
        elif progress_ratio < 0.7:
            # Mid generations: balanced
            k = 4
            e = 3
            m = 0.25
        else:
            # Late generations: exploitation
            k = 6
            e = 4
            m = 0.1
        new_gen = selection(population, fitness_list, days, room_cap_map, fitness_dep, num_timeslots, attempts, k, e, m, assignments, valid_room)
        for chromosome in new_gen:
            fit = fitness(chromosome, fitness_dep, room_cap_map, lec_workload_map, lec_tod_map, mid_day, num_lecturers)
            fit_list.append(fit)
        best_solution, best_fit = get_best_chromosome(new_gen, fit_list)
        print(f"gen: {attempts}, best fitness: {best_fit}")
        final_fitness = best_fit
        final_chromosome = best_solution
        
        # Check for improvement
        if best_fit > best_fitness_history[-1]:
            best_fitness_history.append(best_fit)
            stagnation_counter = 0
        else:
            stagnation_counter += 1
            
        # Early stopping if stagnated
        if stagnation_counter >= stagnation_limit:
            print(f"Stopping due to stagnation after {stagnation_limit} generations without improvement")
            break
            
        if best_fit == 1.0:
            final_chromosome, final_fitness = best_solution, best_fit
            found = True
            population = new_gen
            break
        else:
            population = new_gen
            attempts += 1
        
    best_solution, best_fit = get_best_chromosome(new_gen, fit_list)
    final_fitness = best_fit
    final_chromosome = best_solution
        
    #else:
    #    final_chromosome, final_fitness = get_best_chromosome(fitness_list, population)

    print(f"generations to solution{attempts}, fitness of solution = {final_fitness}\n length of genes = {len(final_chromosome)}")
    periods = get_periods(start_hour, stop_hour)

    #decode chromosome
    decoded_timetable = build_timetable(final_chromosome, courses, lecturers, departments, rooms, periods)

    return decoded_timetable, best_fit