#To build my first mini project(Rock-paper-Scissor) Game
import random
play = "yes"
while play!= "no" :
    my_option = input("Enter your option: Rock or Paper or scissor? ")
    words = ["rock","paper","scissor"]
    if my_option.lower() not in words:
        print("Invalid input !")
        continue
    computer_option = random.choice(words)
    print(f"computer_option is {computer_option}")
    if my_option.lower() == computer_option:
        print("Match Tie")
    elif my_option.lower() == "rock":
        if computer_option == "paper":
            print("Computer wins ")
        elif computer_option == "scissor" :
            print("You win")
    elif my_option.lower() == "paper":
        if computer_option == "rock":
            print("you win")
        elif computer_option == "scissor":
            print("Computer wins")
    else :
        if computer_option == "rock":
            print("Computer wins")
        elif computer_option == "paper" :
            print("You win")
    play = input("Do you want to play again (yes/no)")
