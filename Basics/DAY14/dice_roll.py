#To build a dice roll simulator
import random
roll = "yes"
num = 0
high = 0
while roll == "yes":
    num += 1
    dice = random.randint(1,6)
    print(dice)
    if dice > high:
        high = dice
    roll = input("Do you want to roll again? (yes/no)")
    if roll == "no":
        print(f"No. of rolls = {num}")
        print(f"Highest number rolled is {high} ")
