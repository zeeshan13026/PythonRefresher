# def add(parameter):
#     pass
#
# add(argument)
''' Positional arguments have to go first then keyword arguments later '''
print("*"*30)
def add(x, y):
    result = x + y
    print(result)

add(3, 6)
print("******Positional Arguments************")
def say_hello(name):
    print(f"Hello {name}")

say_hello("Harry")

print("******Keyword Arguments************")
def say_hi(name, surname):
    print(f"Hello {name} {surname}")

say_hi( surname="Ahmad", name="Zeeshan")

