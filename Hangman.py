


import wordslist

import random

chosen_word = random.choice(wordslist.python_fundamentals)
lives = 6

from hangmanart import logo, stages
print(logo)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose")

    if "_" not in display:
        end_of_game == True
        print("You win")

    import hangmanart
    print(stages[lives])

    
