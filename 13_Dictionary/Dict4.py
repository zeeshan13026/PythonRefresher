student_attendance = {"Rolf": 80, "Bob": 75, "Anne": "90"}

# You can check the keys in the dictionary but not the values
if "Bob" in student_attendance:
    print(f"Attendance of Bob is {student_attendance['Bob']}")
else:
    print("Bob is not a student")