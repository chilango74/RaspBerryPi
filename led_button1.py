from gpiozero import LED, Button
from signal import pause

led = LED(4)
button = Button(17)

led.source = button

pause()