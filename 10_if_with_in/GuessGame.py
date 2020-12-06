number = 7
user_input = input("Enter 'y' if you would like to play : ").lower()

if user_input == 'y':
    user_number = int(input("Guess the number : "))
    if user_number == number:
        print("You Guessed correctly !!!")
    elif abs(user_number-number) == 1: # user_number-number in (1,-1)
        print("you are off by 1")
    else:
        print("Sorry, It's wrong")