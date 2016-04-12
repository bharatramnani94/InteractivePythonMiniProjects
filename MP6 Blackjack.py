# Mini-project #6 - Blackjack
# http://www.codeskulptor.org/#user38_U1JiggRvMIYKGOt.py

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_cards = []	# create Hand object

    def __str__(self):
        s = "Hand contains: "
        for i in self.hand_cards:	# return a string representation of a hand
            s += str(i)
            s += " "
        return s

    def add_card(self, card):
        self.hand_cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        aces = 0
        for i in self.hand_cards:
            r = i.get_rank()
            value += VALUES[r]
            if r == 'A':
                aces += 1
        if aces==0:
            return value
        else:
            if (value+10)<=21:
                return (value+10)
            else:
                return value
            
        
        # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in self.hand_cards:
            i.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_cards = []	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                c = Card(i, j)
                self.deck_cards.append(c)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck_cards)
        
    def deal_card(self):
        return self.deck_cards.pop()		# deal a card object from the deck
    
    def __str__(self):
        # return a string representing the deck
        s = "Deck contains "
        for i in self.deck_cards:
            s += str(i)
            s += " "
        return s



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, score

    if in_play == True:
        outcome = "Player quits. New deal?"
        score -= 1
        in_play = False
        return
    
    #print
    #print 'score is', score
    #print

    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    
    #Deal 1st card to both
    c1 = deck.deal_card()
    c2 = deck.deal_card()
    player.add_card(c1)
    dealer.add_card(c2)
    
    #Deal 2nd card to both
    c3 = deck.deal_card()
    c4 = deck.deal_card()
    player.add_card(c3)
    dealer.add_card(c4)
    
    #print both hands
    #print "Player: " + str(player)
    #print "Dealer: " + str(dealer)
    
    in_play = True
    outcome = "Hit or Stand?"

    
def hit():
    global in_play, score, outcome
    
    if in_play == False:
        return;
    
    if player.get_value() <= 21:
        c = deck.deal_card()
        player.add_card(c)
        #print 'Player:', str(player)
 
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    
    if player.get_value() > 21:
        #print "You have busted"
        in_play = False
        score -= 1
        outcome = "Player busted. Dealer won. New deal?"
    
        
def stand():
    global score, in_play, outcome
    
    if in_play == False:
        return;
    
    if player.get_value() > 21:
        #print 'You have busted'
        outcome = "Player busted. Dealer won. New deal?"
    else:
        while (dealer.get_value())<17:
            dealer.add_card(deck.deal_card())
            #print str(dealer)
    
    if dealer.get_value() > 21:
        #print 'Dealer busts'
        score += 1
        outcome = "Dealer busted. Player won. New deal?"
    else:    
        if player.get_value() > dealer.get_value():
            score += 1
            #print 'You won'
            outcome = "Player won. New deal?"
        else:
            score -= 1
            #print 'Dealer won, You lose'
            outcome = "Dealer  won. New deal?"
    in_play = False

    # assign a message to outcome, update in_play and score

    
# draw handler    
def draw(canvas):
    
    canvas.draw_text("BLACKJACK", (160, 50), 44, 'Yellow')
    canvas.draw_text(outcome, (40, 530), 32, 'White')
    canvas.draw_text("Score : " + str(score), (40, 580), 36, 'Blue', 'serif')

    canvas.draw_text("Player", (20, 210), 32, 'Lime')
    canvas.draw_text("Dealer", (20, 390), 32, 'Lime')

    player.draw(canvas, [140,150])
    dealer.draw(canvas, [140,330])
    
    if in_play == True:
        canvas.draw_image(card_back, [36, 48], CARD_SIZE, [176.5,379], CARD_SIZE)

        
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric