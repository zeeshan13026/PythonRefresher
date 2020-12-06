''' It will take y =7 if not given while calling add() method'''
def add(x,y=7):
    sum = x+y
    print(sum)

add(5)
add(5,4)
add(x=10)
add(x=10, y=20)
add(y=5) # It will not work bcz we have to give the value of x
# add(x=5,4) Can't give positional argument after keyword argument
