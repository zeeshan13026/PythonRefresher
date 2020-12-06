number = 7


while True:
    user_input = input("Would you like to play ? (Y/n) : ").lower()

    if user_input == 'n':
        print("Thanks you")
        break
    user_number = int(input("Guess the number : "))
    if user_number == number:
        print("You Guessed correctly !!!")
    elif abs(user_number-number) == 1: # user_number-number in (1,-1)
        print("you are off by 1")
    else:
        print("Sorry, It's wrong")

