people = [('Bob', 42, 'Mechanic'), ('James', 24, 'Artist'),('Harry', 32, 'Lecturer')]

for name, age, job in people:
    print(f"{name} is {age} year old and working as a {job}")

for person in people:
    print(f"Name : {person[0]}, Age : {person[1]}, Profession : {person[2]} ")