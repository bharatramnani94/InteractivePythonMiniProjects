# implementation of card game - Memory
# http://www.codeskulptor.org/#user38_INhmGWdeT37h0bd_1.py

import simplegui
import random

# globals

CARD_WIDTH = 50
HALF_CARD_WIDTH = 25
half_cards1 = range(8)
half_cards2 = range(8)
cards = half_cards1 + half_cards2
visible = [] #contains indices of exposed cards
turns = "Turns = "
turns_counter = 0
state = 0


# helper function to initialize globals
def new_game():
    global exposed, state, turns, turns_counter, visible
    visible = []
    state = 0
    turns_counter = 0
    random.shuffle(cards)
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    turns = "Turns = " + str(turns_counter)
    
     
# define event handlers
def mouseclick(pos):
    global state, visible, turns_counter, turns
    i = 0
    global exposed
    while i<16:
        if pos[0]<(50*(i+1)) and pos[0]>(50*i):
            if exposed[i] == False:
                if state == 0:
                    state = 1
                    exposed[i] = True
                    visible.append(i)
                elif state == 1:
                    state = 2
                    exposed[i] = True
                    visible.append(i)
                    if cards[visible[0]] == cards[visible[1]]:
                        exposed[visible.pop()] = True
                        exposed[visible.pop()] = True
                    turns_counter += 1
                    turns = "Turns = " + str(turns_counter)
                else:
                    state = 1
                    if len(visible) == 2:
                        exposed[visible.pop()] = False
                        exposed[visible.pop()] = False  
                    exposed[i] = True
                    visible.append(i)
                print exposed
        i += 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    label.set_text(turns)
    pos = 15
    i = 0
    while i<16: 
        if exposed[i] == True:
            canvas.draw_text(str(cards[i]), (pos, 65), 42, 'White')
        else:
            canvas.draw_polygon([(i * CARD_WIDTH, 0), ((i * CARD_WIDTH) + CARD_WIDTH, 0),
                                 ((i * CARD_WIDTH) + CARD_WIDTH, 100) ,(i * CARD_WIDTH,100)], 
                                5, 'White', 'Green')
        pos += 50
        i += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label(turns)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()