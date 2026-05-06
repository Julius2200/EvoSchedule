
class Course:
    def __init__(self, id, title, freq, level, host, dept, elective=False):
        self.course_id = id
        self.course_title = title
        self.frequency = freq
        self.level = level
        self.host_department = host
        self.department = dept
        self.is_elective = elective

class Lecturer:
    def __init__(self, id, name, workload, preference):
        self.lecturer_id = id
        self.lecturer_name = name
        self.workload = workload
        self.preference = preference

class Room:
    def __init__(self, id, name, capacity, dept, shared=False):
        self.room_id = id
        self.room_name = name
        self.capacity = capacity
        self.department = dept
        self.is_shared = shared

class Department:
    def __init__(self, id, name):
        self.department_id = id
        self.department_name = name

class Timetable_entry:
    def __init__(self, index, lecturer, room, level, day, period, timeslot, host, departments):
        self.course = index
        self.lecturer_name = lecturer
        self.room_name = room
        self.level = level
        self.day = day
        self.period = period
        self.timeslot = timeslot
        self.host_department = host
        self.departments = departments