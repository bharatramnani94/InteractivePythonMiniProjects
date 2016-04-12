# Rock Paper Scissor Lizard Spock
# http://www.codeskulptor.org/#user37_hQHBU1waDs_0.py

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    
    if name == "rock":
        result_name_to_number = 0
    elif name == "Spock":
        result_name_to_number = 1
    elif name == "paper":
        result_name_to_number = 2
    elif name == "lizard":
        result_name_to_number = 3
    elif name == "scissors":
        result_name_to_number = 4
    else:
        print "Invalid choice"
    return result_name_to_number

    
def number_to_name(number):
    
    if number == 0:
        result_number_to_name = "rock"
    elif number == 1:
        result_number_to_name = "Spock"
    elif number == 2:
        result_number_to_name = "paper"
    elif number == 3:
        result_number_to_name = "lizard"
    elif number == 4:
        result_number_to_name = "scissors"
    else:
        print "Invalid choice"
    return result_number_to_name
    

def rpsls(player_choice): 
    
    print ""

    print "Player chooses", player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5)

    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses", comp_choice

    difference = (comp_number - player_number) % 5

    if difference == 0:
        print "Player and computer tie!"
    elif difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 3 or difference == 4:
        print "Player wins!"
    

    
# test code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")