grades = [35,60,80,100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(f"Average of grade is {total/amount}")

print('*'*30)

# Another way to sum all the elements of a list, set and tuple
total = sum(grades)
print(f"Average of grade is {total/amount}")