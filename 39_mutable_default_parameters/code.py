from typing import List, Optional

class Student:
    def __init__(self, name:str, grades:List[int] = []): # This is bad
        self.name = name
        self.grades = grades

    def take_exam(self,result:int):
        self.grades.append(result)

bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)

# Problem --> Shows grades of sam though sam didn't have any grades
sam = Student("Sam")
print(sam.grades)