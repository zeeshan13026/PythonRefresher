class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (80,68,75,82)

    def average_grades(self):
        return sum(self.grades)/len(self.grades)

student = Student()
print(student.average_grades())