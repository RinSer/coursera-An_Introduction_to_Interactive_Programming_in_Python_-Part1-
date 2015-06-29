# template for "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
position = [65, 135]
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    sec = t % 600
    D = str(sec)[-1] # tenth of seconds
    # seconds' units
    if sec > 9:
        C = str(sec)[-2]
    else:
        C = str(0)
    # seconds' tens
    if sec > 99:
        B = str(sec)[-3]
    else:
        B = str(0)
    # minutes
    minutes = int(t/600)
    A = str(minutes)[-1]
    return A + ':' + B + C + '.' + D
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global runs
    timer.start()
    runs = True
    
def stop():
    global runs
    global x
    global y
    timer.stop()
    if (time % 10) == 0 and runs == True:
        x += 1
    if runs == True:
        y += 1
    runs = False
    
def reset():
    global runs
    global time
    global x
    global y
    timer.stop()
    time = 0
    x = 0
    y = 0
    runs = False

# define event handler for timer with 0.1 sec interval
def step():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position, 50, "Red")
    canvas.draw_text(str(x) + '/' + str(y), [200, 25], 25, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 250, 250)

# register event handlers
frame.add_button('Start', start, 125)
frame.add_button('Stop', stop, 125)
frame.add_button('Reset', reset, 125)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, step)

# start frame
frame.start()

# Please remember to review the grading rubric
