from pathlib import Path

from evdev import InputDevice

def connect_gamepad():
    path = Path('/dev/input/')

    input_list = sorted(Path(path).glob('event*'))

    devices = map(InputDevice, input_list)
    devices = {dev.fd: dev for dev in devices}

    gamepad = None
    for dev in devices.values():
        if dev.name == "Gamepad":
            gamepad = dev
            
    if not gamepad:
        raise Error("Gamepad is not found.")
    else:
        print("Gamepad is found:", gamepad)
    return gamepad