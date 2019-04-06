from microbit import *
from OC05 import OC05

# OC05 instance
OC05 = OC05.OC05()

# configure OC05 with frequency of 60Hz
OC05.init(60)

while True:
    if button_b.is_pressed():
        OC05.setServoPosition(1, 0)     # position servo to the left 
        display.scroll("LEFT")
    elif button_a.is_pressed():
        OC05.setServoPosition(1, 180)   # position servo to the right
        print("RIGHT")
    elif button_a.is_pressed() & button_b.is_pressed():
        OC05.setServoPosition(1, 90)    # position servo in the centre
        display.scroll("CENTRE")