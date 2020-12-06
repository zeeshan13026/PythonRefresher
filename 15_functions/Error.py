friends = ['Rolf', 'Bob']

def add_friend():
    friend_name = input("Enter friend's name: ")

    ''' friends is a local variable not a global variable'''
    #friends = friends + [friend_name]  # It will throw error

    f = friends + [friend_name]
    print(f)

add_friend()