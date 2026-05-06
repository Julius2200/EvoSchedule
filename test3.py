import time
from scheduler.ga_run import run_ga
from utils.test_db import get_table_details, get_num_timeslots, get_days, get_mid_day
from utils.test_db import get_level_list

courses, lecturers, rooms, assignments, departments, time_size, max_gen, max_iter = get_table_details()

level_l = get_level_list()

global_settings = {
    "timeslot_data": {
        "start_hour": 8,
        "stop_hour": 18
    },
    "level_list": level_l,
    "days": 5
}

assignment = {
    "mth111": "John Doe",
    "phy111": "Jane Doe",
    "gst111": "Jack Doe",
    "csc101": "Mary Cainne",
    "csc111": "Max Lenner",
    "csc121": "John Damian",
    "csc181": "Jonathan Calmmer",
    "css101": "Nathan Dam",
    "css111": "Megan Keller",
    "css121": "Vivian Sadist",
    "css181": "Veronica Fisher",
    "int101": "Sam Chaser",
    "int111": "Ruth Veren",
    "int121": "James Ryder",
    "int181": "John Doe",
    "swe101": "Jane Doe",
    "swe111": "Jack Doe",
    "swe121": "Mary Cainne",
    "swe181": "Max Lenner",
    "csc201": "John Damian",
    "csc211": "Jonathan Calmmer",
    "csc281": "Nathan Dam",
    "css201": "Megan Keller",
    "css211": "Vivian Sadist",
    "css281": "Veronica Fisher",
    "int201": "Sam Chaser",
    "int211": "Ruth Veren",
    "int281": "James Ryder",
    "swe201": "John Doe",
    "swe211": "Jane Doe",
    "swe281": "Jack Doe",
    "csc301": "Mary Cainne",
    "csc311": "Max Lenner",
    "csc381": "John Damian",
    "css301": "Jonathan Calmmer",
    "css311": "Nathan Dam",
    "css381": "Megan Keller",
    "int301": "Vivian Sadist",
    "int311": "Veronica Fisher",
    "int381": "Sam Chaser",
    "swe301": "Ruth Veren",
    "swe311": "James Ryder",
    "swe381": "John Doe",
    "csc401": "Jane Doe",
    "csc411": "Jack Doe",
    "csc481": "Mary Cainne",
    "css401": "Max Lenner",
    "css411": "John Damian",
    "css481": "Jonathan Calmmer",
    "int401": "Nathan Dam",
    "int411": "Megan Keller",
    "int481": "Vivian Sadist",
    "swe401": "Veronica Fisher",
    "swe411": "Sam Chaser",
    "swe481": "Ruth Veren",
    "csc491": "James Ryder",
    "css491": "John Doe"
}
start = time.time()

timetable, fitness = run_ga(courses[:10], lecturers, rooms, departments, assignment, global_settings)

for gene in timetable:
    print(f"{gene.course}, {gene.lecturer_name}, {gene.day}, {gene.period} ")


end = time.time()
print(f"\n{fitness}, time taken = {end - start:.4f}")