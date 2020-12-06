numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []

for even in numbers:
    if even%2 == 0:
        evens.append(even)
print(f"Even numbers are {evens}")