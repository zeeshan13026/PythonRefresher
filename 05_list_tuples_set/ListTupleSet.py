l = ["Bob","Anne","Rob"]
t = ("Bob","Anne","Rob")
s = {"Bob","Anne","Rob"}

# list ---> Mutable, Insertion order is preserved
print("************LIST*************")
print(l[0])  # Bob
l.append("Smith")  # ['Bob', 'Anne', 'Rob', 'Smith']
print(l)
l.remove("Bob")  # ['Anne', 'Rob', 'Smith']
print(l)
l.remove(l[2])
print(l)

# tuple ---> Immutable, Insertion order is preserved
print("************TUPLE*************")
print(t[1])  # Anne

# set ---> Mutable, Insertion order is not preserved
print("************SET*************")
print(s)
s.add("Charlie")
print(s)
s.remove("Anne")
print(s)