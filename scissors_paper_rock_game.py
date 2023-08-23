# Describe the rules
# # Rock vs Paper -> Paper wins \n"
#       + "Rock vs Scissors -> Rock wins \n"
#       + "Paper vs Scissors -> Scissor wins
# Getting a user choice
# Checking if the choice correct
# Correspond the choice of the user with a particular number
# Print user's choice
# Getting computer's choice
# Make sure that the comp's choice is different from the user's
# Correspond the choice of the comp with a particular number
# Print computer's choice
# Compare two choices
# Print out the winner
# Ask the usere if they are willing to play again

# Start the game
import random
print('Welcome to the Rock, Scissors, Paper game. The rules are these: ')
print('Rock vs Paper -> Paper wins')
print('Rock vs Scissors -> Rock wins')
print('Paper vs Scissors - > Scossors win')

# Getting a user choice from 1 to 3
users_choice_number = int(
    input('Please enter your choice: 1 -> Rock, 2 -> Paper, 3 -> Scissors: '))
# Make sure the user has made a valid choice
while 0 < users_choice_number > 3:

    users_choice_number = int(
        input('You choice is not valid. Try again: '))
# Map the number to the choice
if users_choice_number == 1:
    users_choice = 'Rock'
elif users_choice_number == 2:
    users_choice = 'Paper'
else:
    users_choice = 'Scissors'

# Print user's choice
print(f'Your choice is {users_choice}')
# Now is the computers' turn to go agead with the choice
print("Now is the turn of the computer: ")

# Generate comp's choice number
comp_choice_number = random.randint(1, 3)
# Map the number to the choice
if comp_choice_number == 1:
    comp_choice = 'rOCK'
elif comp_choice_number == 2:
    comp_choice = 'pAPER'
else:
    comp_choice = 'sCISSORS'
# Print comp's choice
print(f'The computer has chosen {comp_choice}')

# Compare user's and comp's choices

if users_choice_number == 1 and comp_choice_number == 2:
    print('Paper wins =>')
    result = 'pAPER'
if users_choice_number == 2 and comp_choice_number == 1:
    print('Paper wins =>')
    result = 'Paper'

if users_choice_number == comp_choice_number:
    print('If is a draw =>')
    result = 'DRAW'


if users_choice_number == 1 and comp_choice_number == 3:
    print('Rock wins =>')
    result = 'Rock'
if users_choice_number == 3 and comp_choice_number == 1:
    print('Rock wins =>')
    result = 'rOCK'

if users_choice_number == 2 and comp_choice_number == 3:
    print('Scissors win =>')
    result = 'sCISSORS'
if users_choice_number == 3 and comp_choice_number == 2:
    print('Scissors win =>')
    result = 'Scissors'
