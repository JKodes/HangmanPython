


python_fundamentals = ['strings', 'integers', 'float', 'Boolean', 'arrays', 'dictionary', 'set', 'tuples', 
                       'function', 'while loop', 'for loop', 'if statment']

import random

chosen_word = random.choice(python_fundamentals)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)



guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
    
