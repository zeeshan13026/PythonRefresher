print("********** Without str **************")
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

student = Student("Anne",25)
print(student)

''' str is used to represent object'''
print("********** With str **************")
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


student = Student("Anne",25)
print(student)


