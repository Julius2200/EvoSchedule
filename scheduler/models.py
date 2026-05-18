
class Course:
    def __init__(self, id, title, freq, level, host, dept, elective=False):
        self.id = id
        self.title = title
        self.frequency = freq
        self.level = level
        self.host_department = host
        self.department = dept
        self.is_elective = elective

class Lecturer:
    def __init__(self, id, name, workload, preference):
        self.id = id
        self.name = name
        self.workload = workload
        self.preference = preference

class Room:
    def __init__(self, id, name, capacity, dept, shared=False):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.department = dept
        self.is_shared = shared

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Timetable_entry:
    def __init__(self, index, lecturer, room, level, day, period, timeslot, host, departments):
        self.course = index
        self.lecturer = lecturer
        self.room = room
        self.level = level
        self.day = day
        self.period = period
        self.timeslot = timeslot
        self.host_department = host
        self.departments = departments
