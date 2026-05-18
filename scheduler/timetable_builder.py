from scheduler.models import *


def get_particular_day(value):
    day = None
    if value == 0:
        day = "Monday"
    elif value == 1:
        day = "Tuesday"
    elif value == 2:
        day = "Wednesday"
    elif value == 3:
        day = "Thursday"
    else:
        day = "Friday"

    return day


def build_timetable(chromosome, courses, lecturers, departments, rooms, periods):
    timetable_list = []
    
    for gene in chromosome:
        print(gene)
        c_index, l_index, r_index, level, d, time = gene
        d = int(d)
        course = courses[c_index]
        lecturer = lecturers[l_index]
        room = rooms[r_index]
        day = get_particular_day(d)
        period = periods[time]
        course_id = course["id"]
        lecturer_name = lecturer["name"]
        room_name = room["name"]
        host = course["host_department"]
        dept = course["department"]
        timeslot = (d, time)

        new_entry = Timetable_entry(course_id, lecturer_name, room_name, level, day, period, timeslot, host, dept)

        timetable_list.append(new_entry)

    return timetable_list
