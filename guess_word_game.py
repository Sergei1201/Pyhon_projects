import random
# Getting an input from the user
name = input('What is your name?: ')
print(f'Good luck, {name}')

# Generate a random word from a list
words = ['apple', 'banana', 'fruits', 'pineapple', 'pear']

word = random.choice(words)

# Initialize a variable that will represent guesses
print('Guess the character')
guesses = ''

# Loop through the word to compare to find out if the character that the user entered is in the word
# If so, append to guesses, otherwise append _
tries = 10
while tries > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_')
            failed += 1
    if failed == 0:
        print(f'You have won the game. The correct word is {word}')
        break
    guess = input('Guess the character: ')
    guesses += guess
    if guess not in word:
        tries -= 1
        print('You are wrong')
        print(f'You have {tries} left')
        if tries == 0:
            print('You have lost the game')
