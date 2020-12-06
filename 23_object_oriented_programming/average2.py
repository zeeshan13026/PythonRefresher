class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades)/len(self.grades)

student = Student("Anne",(89,20,40,60))
print(student.average_grades())