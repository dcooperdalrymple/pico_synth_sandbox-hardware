import math
import struct
from machine import Pin
from machine import I2S

BITS = 16
SAMPLE_RATE = 22050
CHANNELS = I2S.STEREO

TONE = 440
AMPLITUDE = 3000
SAMPLES = SAMPLE_RATE//TONE

BYTES_PER_SAMPLE = BITS//8
BUFFERS = 1
BUFFER_SIZE = SAMPLES * BYTES_PER_SAMPLE * (CHANNELS+1) * BUFFERS

bus = I2S(
    1, # Bus ID
    sck=Pin(19),
    ws=Pin(20),
    sd=Pin(21),
    mode=I2S.TX,
    bits=BITS,
    format=CHANNELS,
    rate=SAMPLE_RATE,
    ibuf=BUFFER_SIZE
)

buffer = bytearray(BUFFER_SIZE)
for i in range(SAMPLES*BUFFERS):
    sample = int(AMPLITUDE * math.sin(2 * math.pi * i / SAMPLES))
    for j in range(CHANNELS+1):
        struct.pack_into("<h", buffer, i*BYTES_PER_SAMPLE*(CHANNELS+1)+j, sample)

try:
    while True:
        bus.write(buffer)
except (KeyboardInterrupt, Exception) as e:
    print("{}: {}".format(type(e).__name__, e))

bus.deinit()
