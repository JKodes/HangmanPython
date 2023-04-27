import random

import wordslist
chosen_word = random.choice(wordslist.python_fundamentals)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangmanart import logo, stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"
   

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guess {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. For that a life is loss")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

        print(f"{' '.join(display)}")
        
        if "_" not in display:
            end_of_game == True
            print("You win")

        
        print(stages[lives])

    
