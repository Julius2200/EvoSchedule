from utils.models import Timetable_entry
from utils.data_loader import get_day_data

"""
Gene representation for timetable entry:
id
name
name
day
period
department
level
"""

def build_timetable(chromosome, courses, lecturers, rooms, periods):
    timetable = []
    for gene in chromosome:
        c_indx, l_indx, r_indx, day, timeslot = gene
        current_course = courses[c_indx]
        c_id = current_course["id"]
        
        current_lec = lecturers[l_indx]
        l_id = current_lec["name"]

        current_room = rooms[r_indx]
        r_id = current_room["name"]
        current_day = get_day_data(day)
        period = periods[timeslot]
        depts = current_course["department"]
        host = current_course["host_department"]
        lvl = current_course["level"]

        entry = Timetable_entry(c_id, l_id, r_id, current_day, period, host, depts, lvl)

        timetable.append(entry)

    return timetable
