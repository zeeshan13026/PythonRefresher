def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total*arg
    print(total)
    return total

def apply(*args,operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1,3,5,7,operator="*"))

