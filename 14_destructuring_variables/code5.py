head, *tail = [1,2,3,4,5]
print(head)
print(tail)


*head, tail = [1,2,3,4,5]
print(head)
print(tail)

# Blog related to destructuring : https://blog.tecladocode.com/destructuring-in-python/

head, *middle, tail = [1, 2, 3, 4, 5]

print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5