from operator import itemgetter

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

print(search(friends,'Rolf Smith',itemgetter('name')))