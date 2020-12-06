student_attendance = {"Rolf": 80, "Bob": 75, "Anne": "90"}

# Iterating on Keys
for student in student_attendance:
    print(f"{student} : {student_attendance[student]}")
    #print(student)



for student, attendance in student_attendance.items():
    print(student, " --- ", attendance)



