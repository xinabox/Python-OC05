from xOC05 import xOC05
from xCore import xCore

# OC05 instance
OC05 = xOC05()

# configure OC05 with frequency of 60Hz
OC05.init(60)

while True:
    OC05.setServoPosition(1, 0)     #  position servo to the right 
    xCore.sleep(50)
    OC05.setServoPosition(1, 180)   #  position servo to the left
    xCore.sleep(50)
