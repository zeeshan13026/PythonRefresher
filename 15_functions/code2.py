def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_second = user_age * 365 * 24 *60 *60
    print(f"Your age in seconds {age_second}")

user_age_in_seconds()