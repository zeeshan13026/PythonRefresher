users = [
    (0, 'Bob', 'Bob123'),
    (1, 'Rolf', 'R123'),
    (2, 'Anne', 'Anne@123'),
    (3, 'Username', 'Password')
]

username_mapping = {user[1]: user for user in users}
# print(username_mapping)
# print(username_mapping["Bob"])

username_input = input(" Enter user name : ")
password_input = input("Enter password")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct")
else:
    print("Your details are incorrect")





# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {"name": "Jose", "school": "Computing", "grades": (66,77,88)}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data["grades"] # Change this!
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total+=sum(student["grades"])
        count+=len(student["grades"])
        # Implement here

    return total / count