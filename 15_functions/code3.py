def add_friend():
    user_friend = input("Enter friend name : ")
    friend.append(user_friend)

friend = [] # It's work but we have to define global variable at the top

add_friend()

print(friend)