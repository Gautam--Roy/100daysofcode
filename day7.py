# step 1

import random
from logo import logo
from stages import stages
from word_list import word_list

print(logo)

chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
lives = 7


while not end_of_game:
    guess = (input("Guess a letter: ")).lower()

    if guess in display:
        print(f"You've already guessed the letter {guess}. Try a different letter")

    if guess not in chosen_word:
        print(f"You've guessed {guess}. It's not in the word. You lose a life.")
        print(stages[len(stages) - lives])
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You Lose! The word was {chosen_word}")

    for position in range(len(chosen_word)):
        if chosen_word[position].lower() == guess.lower():
            display[position] = guess.lower()

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")
