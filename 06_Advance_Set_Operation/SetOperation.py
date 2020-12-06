print("************DIFFERENCE************")
friends = {"Bob","Max","Jim"}
abroad = {"Bob", "Jim"}

local_friend = friends.difference(abroad)  # friends - abroad
print(f"{local_friend} is my Local frind")

# Union
print("************UNION************")
local = {"Max"}
abroad2 = {"Bob", "Jim"}
totalFriends = local.union(abroad2)
print("Total friends : ",totalFriends)

# Intersection
print("************INTERSECTION************")
art = {'Amy','Jan','Ron','Tom'}
science = {'Amy', 'Ron', 'Kat', 'Sam'}
both = art.intersection(science)
print("Both subjects : ",both)

