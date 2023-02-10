from gpiozero import LED, Button
from signal import pause

led = LED(4)
button = Button(17)


def press_button():
    led.blink(on_time=1, off_time=1, n=5, background=False)
    print("pressed")

button.when_pressed = press_button
button.when_released = led.off

pause()