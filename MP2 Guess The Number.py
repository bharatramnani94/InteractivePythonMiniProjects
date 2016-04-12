# GUESS THE NUMBER
# http://www.codeskulptor.org/#user38_QNf4r22EQT0nhv7.py

import simplegui
import random


# global variables
range_higher_limit = 100


# helper function to start and restart the game
def new_game():
    global secret_number
    global number_of_attempts_remaining
    if range_higher_limit == 1000:
        number_of_attempts_remaining = 10
    elif range_higher_limit == 100:
        number_of_attempts_remaining = 7
    secret_number = random.randrange(0, range_higher_limit)
    print ""
    print "New game. Range is from 0 to", range_higher_limit
    print "Number of remaining guesses is", number_of_attempts_remaining


# define event handlers for control panel
def range100():
    global range_higher_limit
    range_higher_limit = 100    
    new_game()

def range1000():
    global range_higher_limit
    range_higher_limit = 1000 
    new_game()
    
def input_guess(guess):
    global number_of_attempts_remaining
    print ""
    n = int(guess)
    print "Guess was", n
    number_of_attempts_remaining -= 1
    print "Number of remaining guesses is", number_of_attempts_remaining
    if n>secret_number:
        print "Lower!"
        if number_of_attempts_remaining == 0:
            game_over()
    elif n<secret_number:
        print "Higher!"
        if number_of_attempts_remaining == 0:
            game_over()
    else:
        print "Correct!"
        new_game()

def game_over():
    print "You ran out of guesses"
    new_game()
    
# create frame
frame = simplegui.create_frame('Guess The Number', 200, 200)

                      
# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game 
new_game()