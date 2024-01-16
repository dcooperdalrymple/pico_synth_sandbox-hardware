import board
import digitalio
from adafruit_debouncer import Debouncer
import rotaryio

def get_button(pin):
    input = digitalio.DigitalInOut(pin)
    input.direction = digitalio.Direction.INPUT
    input.pull = digitalio.Pull.UP
    return Debouncer(input)

button = (
    get_button(board.GP13),
    get_button(board.GP18)
)
encoder = (
    rotaryio.IncrementalEncoder(board.GP12, board.GP11),
    rotaryio.IncrementalEncoder(board.GP17, board.GP16)
)
last_position = [encoder[0].position, encoder[1].position]

while True:
    for i in range(2):
        current_position = encoder[i].position
        if current_position - last_position[i] != 0:
            print("{:d}: {:d}".format(i+1, current_position))
        last_position[i] = current_position

        button[i].update()
        if button[i].fell:
            print("{:d}: press".format(i+1))
        if button[i].rose:
            print("{:d}: release".format(i+1))
