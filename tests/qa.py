import board
import adafruit_character_lcd.character_lcd as characterlcd
import digitalio
from adafruit_debouncer import Debouncer
import rotaryio
import touchio

# Character LCD
lcd_rs = digitalio.DigitalInOut(board.GP20)
lcd_en = digitalio.DigitalInOut(board.GP21)
lcd_d4 = digitalio.DigitalInOut(board.GP22)
lcd_d5 = digitalio.DigitalInOut(board.GP26)
lcd_d6 = digitalio.DigitalInOut(board.GP27)
lcd_d7 = digitalio.DigitalInOut(board.GP28)
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 16, 2)

def lcd_print(name, value):
    lcd.clear()
    lcd.message = name + "\n" + value

lcd.cursor = False
lcd.blink = False
lcd_print("PicoSynthSandbox", "Rev1 2023-09-14")

# Encoder
button_pin = digitalio.DigitalInOut(board.GP2)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP
button_switch = Debouncer(button_pin)

encoder = rotaryio.IncrementalEncoder(board.GP1, board.GP0)
last_position = encoder.position

# Keyboard
class Key:
    def __init__(self, name, pin):
        self.name = name
        self.switch = Debouncer(touchio.TouchIn(pin))
    def update(self):
        self.switch.update()
        if self.switch.rose:
            lcd_print("Keyboard", self.name + " Pressed")
        if self.switch.fell:
            lcd_print("Keyboard", self.name + " Released")

keys = [
    Key("C", board.GP16),
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
    current_position = encoder.position
    if current_position - last_position != 0:
        lcd_print("Encoder", str(current_position))
    last_position = current_position

    button_switch.update()
    if button_switch.fell:
        lcd_print("Encoder", "Press")
    if button_switch.rose:
        lcd_print("Encoder", "Release")

    for key in keys:
        key.update()
