import gpiozero
import time

robot = gpiozero.Robot(left=(17, 18), right=(27, 22))

for i in range(1, 3):
    robot.forward()
    time.sleep(5)
    
    robot.left()
    time.sleep(2)
    
    robot.backward()
    time.sleep(5)
robot.stop()