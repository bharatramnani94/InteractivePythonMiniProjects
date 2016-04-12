# "Stopwatch: The Game"
# http://www.codeskulptor.org/#user38_8zQUGxReasA1wst.py

import simplegui

# define global variables
time = 0
success = 0
attempts = 0
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ms = t%10
    s = t/10
    s = s%60
    if s<10:
        string_s = "0" + str(s)
    else:
        string_s = str(s)

    if t<100:
        return "0:" + string_s + "." + str(ms)
    elif t<600:
        return "0:" + string_s + "." + str(ms)
    else:
        min = t/600
        return str(min) + ":" + string_s + "." + str(ms)
        
    
# define event handlers for buttons: "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    global timer_running
    timer_running = True
    
def stop_handler():
    timer.stop()
    global success, attempts, timer_running
    if (timer_running == True):
        if time%10==0:
            success += 1
        attempts += 1
    timer_running = False
    
def reset_handler():
    global time, success, attempts
    timer.stop()
    time = 0
    success = 0
    attempts = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (100, 120), 48, 'White')
    canvas.draw_text(str(success) + "/" + str(attempts), (245, 40), 32, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 200)
start_button = frame.add_button('Start', start_handler, 150)
stop_button = frame.add_button('Stop', stop_handler, 150)
reset_button = frame.add_button('Reset', reset_handler, 150)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
timer = simplegui.create_timer(100, timer_handler)
frame.start()


# Please remember to review the grading rubric