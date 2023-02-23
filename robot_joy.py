import time

import gpiozero
from Gamepad import Gamepad

cpu = gpiozero.CPUTemperature(min_temp=20, max_temp=80)

# Gamepad settings

buttonExit = 'START'
buttonStop = 'B'

x_axes = 'LEFT_X'
y_axes = 'LEFT_Y'

pollInterval = 0.1

# Wait for a connection
if not Gamepad.available():
    print('Please connect your gamepad...')
    while not Gamepad.available():
        time.sleep(1.0)
print('Gamepad connected')

# Set some initial state
speed = 0.0
steering = 0.0

gamepad = Gamepad.DefenderX7()
# Start the background updating
gamepad.startBackgroundUpdates()

robot = gpiozero.Robot(left=(17, 18), right=(27, 22))

# Joystick events handled in the background
try:
    while gamepad.isConnected():
        if cpu.temperature > 50:
            print(f'WARNING: Temperature is above 50C')
        # Check for the exit button
        if gamepad.beenPressed(buttonExit):
            robot.stop()
            print('EXIT')
            break
        
        if gamepad.beenPressed(buttonStop):
            robot.stop()
            print('STOP')
          
        forward_value = gamepad.axis(y_axes)
        turn_value = gamepad.axis(x_axes)
        
        # print(f'{forward_value=}, {turn_value=}')
        if turn_value < 0.3 and turn_value > -0.3:
            # print('moving forward')
            robot.value = forward_value, forward_value
        else:
            # print('turning')
            robot.value = turn_value/2, -turn_value/2
        
            
        # Sleep for our polling interval
        time.sleep(pollInterval)
            
finally:
    # Ensure the background thread is always terminated when we are done
    robot.stop()
    gamepad.disconnect()
            
        

        