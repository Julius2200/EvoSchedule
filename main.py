import time
from algorithm.genetic_algo import run_ga
from algorithm.timetable_builder import build_timetable
from utils.test_db import get_table_details
from utils.test_db import get_level_list
from utils.timeslots import generate_periods


def get_class_size(level_list, keys, index):
    total = 0
    for item in keys:
        current_item = level_list[item]
        #print(type(level_list))
        total += current_item[index]

    return total

def calc_utilization(rooms, num_timeslot, chromosome):
    value = len(chromosome)
    print(value)
    quotient = 0
    for room in rooms:
        quotient += (5 * num_timeslot)

    result = value/quotient

    return result


courses, lecturers, rooms, assignments, dept, num_timeslots, max_gen, max_iter = get_table_details()
level_list = get_level_list()
num_timeslots = 10

start = time.time()
chromosome, generations = run_ga(courses[:20], lecturers[:], rooms, assignments, dept, level_list, num_timeslots, max_gen, max_iter)
c, s = chromosome
print(f"No of Generations {generations}\nFitness score: {s}")

#end = time.time()
#print(f"Duration: {end - start: .4f}s")

periods = generate_periods(8, 18)
table = build_timetable(c, courses, lecturers, rooms, periods)
for gene in table:
    print(f"{gene.day} {gene.period}| {gene.course_id}| {gene.departments}| {gene.level}\n")

end = time.time()
print(f"Duration: {end - start:.4f}")

util_rate = calc_utilization(rooms, num_timeslots, c)
print(f"Utilization Rate = {util_rate * 100:.4f}")