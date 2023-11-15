# pico_synth_sandbox/touch-keyboard.py
# 2023 Cooper Dalrymple - me@dcdalrymple.com
# GPL v3 License

import board, time
from digitalio import DigitalInOut, Direction, Pull

MODE_8KEY=0
MODE_16KEY=1

input_mode = MODE_16KEY
input_bits = (input_mode + 1) * 8

sdo = DigitalInOut(board.GP6)
sdo.direction = Direction.INPUT
sdo.pull = Pull.UP

scl = DigitalInOut(board.GP7)
scl.direction = Direction.OUTPUT

def sleep_us(us):
    ns = us * 1000
    t = time.monotonic_ns()
    while time.monotonic_ns() - t < ns:
        pass
def sleep_ms(ms):
    s = ms / 1000.0
    t = time.monotonic()
    while time.monotonic() - t < s:
        pass

while True:
    data = 0
    scl.value = True
    for i in range(input_bits):
        scl.value = False
        if sdo.value:
            data |= (1 << i)
        scl.value = True
    scl.value = False
    print(bin(data))
    time.sleep(0.5)
