class Course:
    def __init__(self, c_id, dept, host, level, frequency, elective, group):
        self.course_id = c_id
        self.departments = dept #list
        self.host_department = host #host department
        self.level = level
        self.frequency = frequency
        self.is_elective = elective #true or false
        self.elective_group = group #None or group name

class Room:
    def __init__(self, r_name, dept, cap, shared):
        self.room_name = r_name
        self.departments = dept
        self.capacity = cap
        self.is_shared = shared #true or false

class Lecturer:
    def __init__(self, name, workload):
        self.lecturer_name = name
        self.workload = workload

class Timetable_entry:
    def __init__(self, c_id, lec_name, r_name, day, period, host, depts, level):
        self.course_id = c_id
        self.lecturer_name = lec_name
        self.room_name = r_name
        self.day = day
        self.period = period
        self.host_department = host
        self.departments = depts
        self.level = level