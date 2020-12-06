def search(sequence,expected, finder):
    for ele in sequence:
        if finder(ele) == expected:
            return ele
    raise RuntimeError(f"couldn't find an element with {expected}")

friends = [
    {"name":"Rolf Smith", "age":25},
    {"name":"Adam wool", "age":29},
    {"name":"Anne pun", "age":21}
]

def get_friend_name(friend):
    return friend['name']


print(search(friends, "Rolf Smith", get_friend_name))

# Can also do this instead of line (13 - 17 )
#print(search(friends, "Rolf Smith", lambda friend:friend['name']))