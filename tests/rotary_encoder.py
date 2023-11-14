import board
import digitalio
from adafruit_debouncer import Debouncer
import rotaryio

button_pin = digitalio.DigitalInOut(board.GP2)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP
button_switch = Debouncer(button_pin)

encoder = rotaryio.IncrementalEncoder(board.GP1, board.GP0)
last_position = encoder.position

while True:
    current_position = encoder.position
    if current_position - last_position != 0:
        print(current_position)
    last_position = current_position

    button_switch.update()
    if button_switch.fell:
        print("press")
    if button_switch.rose:
        print("release")
