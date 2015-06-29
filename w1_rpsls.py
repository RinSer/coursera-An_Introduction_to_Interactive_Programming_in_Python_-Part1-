# Mini-Project Week 1
# My Rock-Paper-Scissors-Lizard-Spock Game
# I have tried to indulge you, my esteemed peer and
# printed 5 cases you have to examine in the bottom of my code,
# so you can check them by just clicking play button.
# Hope that you appreciate it! (;

import random

# Helper function to assign numbers to corresponding names
def name_to_number(name):
    """
    The function that assigns numbers to names.
    """
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print 'Wrong name value, choose from: "rock, scissors, paper, lizard, Spock".'
        
    return number

# Helper function to assign names to corresponding numbers
def number_to_name(number):
    """
    The function that assigns names to numbers.
    """
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print 'Wrong number value, choose any whole number from 0 to 4.'
        
    return name

# Main function for the game
def rpsls(player_choice):
    """
    The function that executes the game.
    """
    # Output player's choice
    print ''
    print 'Player chooses', player_choice
    player_number = name_to_number(player_choice)
    # Make computer's random decision
    comp_number = random.randrange(0, 5)
    comp_choise = number_to_name(comp_number)
    print 'Computer chooses', comp_choise
    # The game outcomes
    win = (comp_number - player_number) % 5
    if win == 0:
        return 'Player and computer tie!'
    elif win == 1 or win == 2:
        return 'Computer wins!'
    else:
        return 'Player wins!'
    
    
# Testing 5 cases:
print rpsls('rock')
print rpsls('Spock')
print rpsls('paper')
print rpsls('lizard')
print rpsls('scissors')