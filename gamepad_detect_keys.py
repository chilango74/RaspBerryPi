from evdev import InputDevice, categorize, ecodes, KeyEvent
from connect_gamepad import connect_gamepad

gamepad = connect_gamepad()

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        print(keyevent)
