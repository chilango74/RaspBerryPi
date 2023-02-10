from evdev import InputDevice, categorize, ecodes, KeyEvent
import gpiozero
import time

from connect_gamepad import connect_gamepad

gamepad = connect_gamepad()

robot = gpiozero.Robot(left=(17, 18), right=(27, 22))

print(gamepad)
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == 308:  # BTN_Y
                print('Forward')
                robot.forward(0.3)
            elif keyevent.scancode == 304:  # BTN_A
                print('Back')
                robot.backward(0.3)
            elif keyevent.scancode == 307:  # BTN_X
                print('Left')
                robot.left(0.3)
            elif keyevent.scancode == 305:  # BTN_B
                print('Right')
                robot.right(0.3)
            else:
                print('Stop')
                robot.stop()
