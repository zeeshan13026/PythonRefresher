'''Normal Function'''

def sum(x,y):
    return x+y

print(sum(4,5))

'''Lambda Function'''
# Function without name
add = lambda x,y:x+y
print(add(3,17))

# Another way to use lambda function ---> Not use commonly
print((lambda x,y:x*y)(2,5))