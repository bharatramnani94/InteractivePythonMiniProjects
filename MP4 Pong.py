# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user38_ogKyW7tU45jrxf2.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,0]  

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(2, 4)
    if direction == "LEFT":
        ball_vel[0] = random.randrange(-3, -1)
    ball_vel[1] = random.randrange(-4,-1)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball("RIGHT")
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # detect top,down collisions
    if ball_pos[1] <= (BALL_RADIUS/2 + 7):
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= HEIGHT - (BALL_RADIUS/2 + 7):
        ball_vel[1] = -ball_vel[1]
        
    # detect left,right collisions with gutter
    if ball_pos[0] <= (BALL_RADIUS/2 + PAD_WIDTH + 7):
        if (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT) and (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += (ball_vel[0]/10)
        else:
            spawn_ball("RIGHT") 
            score2 += 1
            
    if ball_pos[0] >= WIDTH - (BALL_RADIUS/2 + PAD_WIDTH + 7):
        if (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT) and (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] += (ball_vel[0]/10)
        else:
            spawn_ball("LEFT")
            score1 += 1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos <= (HALF_PAD_HEIGHT + 6):
        paddle1_pos = (HALF_PAD_HEIGHT + 6)
    if paddle1_pos >= HEIGHT - (HALF_PAD_HEIGHT + 6):
        paddle1_pos = HEIGHT - (HALF_PAD_HEIGHT + 6)
    if paddle2_pos <= (HALF_PAD_HEIGHT + 6):
        paddle2_pos = (HALF_PAD_HEIGHT + 6)
    if paddle2_pos >= HEIGHT - (HALF_PAD_HEIGHT + 6):
        paddle2_pos = HEIGHT - (HALF_PAD_HEIGHT + 6)
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]], 8, 'Yellow', 'Orange')
    canvas.draw_polygon([[WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], 8, 'Yellow', 'Orange')
    
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/2 - 80, 75], 44, 'White')
    canvas.draw_text(str(score2), [WIDTH/2 + 50, 75], 44, 'White')

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += 5
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += 5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel -= 5
        
def restart_handler():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
frame.add_button('Restart', restart_handler, 100)
