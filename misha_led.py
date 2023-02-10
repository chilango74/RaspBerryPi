import gpiozero
import time

l = gpiozero.LED(4)

l.on()
time.sleep(1)
l.off()

time.sleep(2)

l.on()
time.sleep(5)
l.off()
