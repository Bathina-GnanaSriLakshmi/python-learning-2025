#To build a number guessing game
num = 0
while num != 42:
    num = int(input("Guess the number: "))
    if num>42:
        print(f"The number is less than {num}")
    elif num <42:
        print(f"The number is greater than {num}")
    if num == 42:
        print("You guessed the right number")