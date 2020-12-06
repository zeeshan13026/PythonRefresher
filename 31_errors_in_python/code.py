def divide(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can't be 0")
    return dividend/divisor

grades = []

try:
    average = divide(sum(grades),len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list.")
else:
    print("your grades average is ",average)
finally:
    print("Thankyou")


