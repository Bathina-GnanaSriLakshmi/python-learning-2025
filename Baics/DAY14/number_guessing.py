#To build a number guessing game
import random
random_num = random.randint(1,100)
num = 0
count = 0
while random_num != num:
    count += 1
    num = int(input("Guess the number: "))
    if num> random_num :
        print(f"Required number is less than {num}")
    elif num < random_num :
        print(f"Required number is greater than {num}")
    else :
        print(f"You have guessed the number in {count} attempts")