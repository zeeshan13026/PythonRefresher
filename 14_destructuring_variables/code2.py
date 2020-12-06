student_attendance = {"Rolf": 80, "Bob": 75, "Anne": 90}

print(list(student_attendance.items()))  # It returns a list of tuples

for t in student_attendance.items():
    print(t) # returns a tuple
