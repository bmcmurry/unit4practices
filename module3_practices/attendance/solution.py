class AttendanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            raise ValueError("Student already exists")
        self.students[name] = [name, False]

    def check_in(self, name):
        if name not in self.students:
            raise ValueError("Student does not exist")
        self.students[name][1] = True

    def delete_student(self, name):
        if name not in self.students:
            raise ValueError("Student does not exist")
        del self.students[name]
