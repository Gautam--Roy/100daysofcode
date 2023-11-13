# Project - Rock, Paper, Scissors

import random

selections = ["rock", "paper", "scissors"]
user_selection = int(input("Choose a number. 0 for rock, 1 for paper, 2 for scissors: "))

computer_selection = random.randint(0,2)

if user_selection > 2 or user_selection < 0:
    print("Invalid choice! Exiting game!")
    exit(0)

print(f"You chose: {selections[user_selection]}")
print(f"Computer chose: {selections[computer_selection]}")

if user_selection == computer_selection:
    print("It's a tie!")
elif (user_selection == 0 and computer_selection == 2) or (user_selection == 1 and computer_selection == 0) or (user_selection == 2 and computer_selection == 1):
    print("You win!")
else:
    print("You lose!")
