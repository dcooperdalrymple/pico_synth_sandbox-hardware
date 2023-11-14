import time
import board
import busio
import adafruit_midi

from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.timing_clock import TimingClock

uart = busio.UART(board.GP4, board.GP5, baudrate=31250, timeout=0.001)
midi = adafruit_midi.MIDI(
    midi_in=uart,
    in_channel=0
)

print("Midi Input Test")
print("Channel:", midi.in_channel + 1)

while True:
    msg = midi.receive()
    if msg is not None:
        print(time.monotonic(), msg)
