''' **kwargs will take multiple arguments as key-value and return dictionary '''

# Packing a dictionary
print("************* Packing ************")
def named(**kwargs):
    print(kwargs)

named(name='Bob',age=25)

# Unpacking a dictionary
print("************* Unpacking ************")
def named(name,age):
    print(name , age)

details = {"name":"Bob", "age":25}
# named(details,26)
named(**details)  # It unpacks the dictionary and treats dictionary as named arguments to the function "named"

print("************* Packing Unpacking ************")
def named(**kwargs):
    print(kwargs)

details = {"name":"Bob", "age":25}
named(**details)