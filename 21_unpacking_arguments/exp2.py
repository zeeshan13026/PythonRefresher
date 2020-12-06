def add(x, y):
    return x + y


num = [2, 4]
print(add(*num))

print("********* kwargs ***********")
nums = {'x': 5, 'y': 7}
print(add(**nums))
# print(add(nums['x'], nums['y'])) Another way