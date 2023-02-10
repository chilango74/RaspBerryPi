import gpiozero

button = gpiozero.Button(17)

while True:
    if button.is_pressed:
        print("button pressed")
    else:
        print("button is not pressed")