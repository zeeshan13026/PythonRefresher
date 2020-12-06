friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = []

for friend in friends:
    if friend.startswith('S'):
        starts_s.append(friend)

print(f"Start with s {starts_s}")

# Using list comprehension
starts_s = [friend  for friend in friends if friend.startswith('S')]
print(starts_s)

