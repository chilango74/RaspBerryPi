import gpiozero
import time

l = gpiozero.LED(4)

def blink(t):
    l.on()
    time.sleep(t)
    l.off()
    
blink(2)
time.sleep(2)
blink(2)
