


python_fundamentals = ['strings', 'integers', 'float', 'Boolean', 'arrays', 'dictionary', 'set', 'tuples', 
                       'function', 'while loop', 'for loop', 'if statment']

import random

chosen_word = random.choice(python_fundamentals)



guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
