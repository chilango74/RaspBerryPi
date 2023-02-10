import gpiozero
import time

robot = gpiozero.Robot(left=(17, 18), right=(27, 22))


robot.forward(0.3)
time.sleep(5)

robot.right()
time.sleep(5)

robot.left()
time.sleep(1)

robot.stop()
