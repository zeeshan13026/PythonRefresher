def add(x, y):
    print(x + y)


add(8, 5)

print(add(8, 5))  # It will print 13 and None bcz we are not returning anything and function return None by default

print("*" * 50)
def sum(x, y):
    return x + y

sum(8, 6)
result = sum(8, 6)
print(result)

'''Print sum twice'''
print("*" * 50)
def sum(x, y):

    print(x+y)
    return x + y

result = sum(8, 9)
print(result)