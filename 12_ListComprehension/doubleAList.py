numbers = [2,3,4,5,6,7]
double = []

# One Way
for number in numbers:
    double.append(number*2)

print(f"New List : {double}")

# Secoond way using list comprehension
print("*"*30)

double = [x * 2 for x in numbers]
print(f"New List using list comprehension : {double}")