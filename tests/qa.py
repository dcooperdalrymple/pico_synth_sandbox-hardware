import board
import adafruit_character_lcd.character_lcd as characterlcd
from digitalio import DigitalInOut, Direction, Pull
from rotaryio import IncrementalEncoder
from adafruit_debouncer import Debouncer
import rotaryio
import touchio
import audiobusio
import audiomixer
import synthio
import busio
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

# Character LCD
lcd_rs = DigitalInOut(board.GP7)
lcd_en = DigitalInOut(board.GP6)
lcd_d4 = DigitalInOut(board.GP22)
lcd_d5 = DigitalInOut(board.GP26)
lcd_d6 = DigitalInOut(board.GP27)
lcd_d7 = DigitalInOut(board.GP28)
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 16, 2)

def lcd_print(name, value):
    lcd.clear()
    lcd.message = name + "\n" + value

lcd.cursor = False
lcd.blink = False
lcd_print("PicoSynthSandbox", "Rev2 2024-01-25")

# Encoder
def get_button(pin):
    input = DigitalInOut(pin)
    input.direction = Direction.INPUT
    input.pull = Pull.UP
    return Debouncer(input)

button = (
    get_button(board.GP13),
    get_button(board.GP18)
)
encoder = (
    IncrementalEncoder(board.GP12, board.GP11),
    IncrementalEncoder(board.GP17, board.GP16)
)
last_position = [encoder[0].position, encoder[1].position]

def update_encoders():
    for i in range(2):
        current_position = encoder[i].position
        if current_position - last_position[i] != 0:
            lcd_print("Encoder {:d}".format(i+1), str(current_position))
        last_position[i] = current_position

        button[i].update()
        if button[i].fell:
            lcd_print("Encoder {:d}".format(i+1), "Press")
        if button[i].rose:
            lcd_print("Encoder {:d}".format(i+1), "Release")

# MIDI
uart = busio.UART(board.GP4, board.GP5, baudrate=31250, timeout=0.001)
midi = adafruit_midi.MIDI(
    midi_in=uart,
    in_channel=0,
    midi_out=uart,
    out_channel=0
)

# Audio
audio = audiobusio.I2SOut(
    bit_clock=board.GP19,
    word_select=board.GP20,
    data=board.GP21
)
mixer = audiomixer.Mixer(
    channel_count=2,
    sample_rate=44100,
    buffer_size=2048
)
audio.play(mixer)
synth = synthio.Synthesizer(
    channel_count=2,
    sample_rate=44100,
    envelope=synthio.Envelope(
        attack_time=0.025,
        attack_level=0.8,
        decay_time=0.025,
        sustain_level=0.4,
        release_time=0.2
    )
)
mixer.voice[0].play(synth)
mixer.voice[0].level = 0.5

# Keyboard
sdo = DigitalInOut(board.GP14)
sdo.direction = Direction.INPUT
sdo.pull = Pull.UP

scl = DigitalInOut(board.GP15)
scl.direction = Direction.OUTPUT

keyboard_data = 0

class Key:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.bit = 1 << index
        self.switch = Debouncer(self.read)
    def read(self):
        global keyboard_data
        return bool(keyboard_data & self.bit)
    def get_notenum(self):
        return 59+self.index
    def update(self):
        self.switch.update()
        if self.switch.rose:
            lcd_print("Keyboard", self.name + " Pressed")
            synth.press(self.get_notenum())
            midi.send(NoteOn(self.get_notenum(), 20))
        if self.switch.fell:
            lcd_print("Keyboard", self.name + " Released")
            synth.release(self.get_notenum())
            midi.send(NoteOff(self.get_notenum(), 0))

keys = [
    Key("B", 0),
    Key("C", 1),
    Key("C#", 2),
    Key("D", 3),
    Key("D#", 4),
    Key("E", 5),
    Key("F", 6),
    Key("F#", 7),
    Key("G", 8),
    Key("G#", 9),
    Key("A", 10),
    Key("A#", 11),
    Key("B", 12),
    Key("C", 13),
    Key("C#", 14),
    Key("D", 15)
]

def update_keyboard():
    global keyboard_data
    keyboard_data = 0
    scl.value = False
    for i in range(16):
        scl.value = True
        if sdo.value:
            keyboard_data |= (1 << i)
        scl.value = False
    scl.value = True
    for key in keys:
        key.update()

# Main Loop

while True:
    update_encoders()
    update_keyboard()
    
    msg = midi.receive()
    if msg is not None:
        if isinstance(msg, NoteOn):
            if msg.velocity > 0:
                synth.press(msg.note)
            else:
                synth.release(msg.note)
        elif isinstance(msg, NoteOff):
            synth.release(msg.note)
