from gpiozero import Motor
import time

motor = Motor(27, 22)
motor.forward()
time.sleep(2)

motor.backward()
time.sleep(2)

motor.stop()