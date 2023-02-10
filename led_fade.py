from gpiozero import PWMLED
from signal import pause

led = PWMLED(4)

led.pulse(fade_in_time=3, fade_out_time=3, n=None, background=True)

pause()