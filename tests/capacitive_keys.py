import time
import board
import touchio
from adafruit_debouncer import Debouncer

class Key:
    def __init__(self, name, pin):
        self.name = name
        self.switch = Debouncer(touchio.TouchIn(pin))
    def update(self):
        self.switch.update()
        if self.switch.rose:
            print(self.name + " pressed")
        if self.switch.fell:
            print(self.name + " released")

keys = [
    Key("C", board.GP19),
    Key("C#", board.GP3),
    Key("D", board.GP6),
    Key("D#", board.GP7),
    Key("E", board.GP8),
    Key("F", board.GP9),
    Key("F#", board.GP10),
    Key("G", board.GP11),
    Key("G#", board.GP12),
    Key("A", board.GP13),
    Key("A#", board.GP14),
    Key("B", board.GP15)
]

while True:
    for key in keys:
        key.update()
