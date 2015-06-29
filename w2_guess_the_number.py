# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# Random number range limits
lower = 0
higher = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global n

    approximate_n = math.log(higher - lower + 1, 2)
    n = int(math.ceil(approximate_n))
    
    print "New game. Range is from 0 to", higher
    print "Number of remaining guesses is", n
    print ""

    secret_number = random.randrange(lower, higher)
    return secret_number

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global higher
    higher = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global higher
    higher = 1000
    new_game()
    
def input_guess(guess):
    """ Converts user input to integer and prints message """
    guess_number = int(guess)
    global n
    n -= 1
    print "Guess was", guess_number
    # Branches
    if guess_number < secret_number and n > 0:
        print "Number of remaining guesses is", n
        print "Higher!"
        print ""
    elif guess_number > secret_number and n > 0:
        print "Number of remaining guesses is", n
        print "Lower!"
        print ""
    elif guess_number == secret_number and n >= 0:
        print "Number of remaining guesses is", n
        print "Correct!"
        print ""
        new_game()
    else:
        print "Number of remaining guesses is", n
        print "You ran out of guesses. The number was", secret_number
        print ""
        new_game()

    
# create frame
frame = simplegui.create_frame("Guess the number", 250, 250)

# register event handlers for control elements and start frame
frame.add_input("Guess the number", input_guess, 200)
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
