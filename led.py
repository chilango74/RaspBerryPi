import gpiozero
import time

led = gpiozero.LED(4)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    print("here")