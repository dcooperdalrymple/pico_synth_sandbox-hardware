# Use the Arduino IDE Serial Plotter to view level data

from machine import Pin
from machine import I2S
import struct

BUFFER_SIZE = 2048
BITS = 16
SAMPLE_RATE = 22050
CHANNELS = I2S.STEREO

FORMAT = ">h" # '>' = big endian, 'h' = short int
DATA_SIZE = struct.calcsize(FORMAT)
BUFFER_SAMPLES = BUFFER_SIZE//DATA_SIZE//(CHANNELS+1)

bus = I2S(
    0, # Bus ID
    sck=Pin(8),
    ws=Pin(9),
    sd=Pin(10),
    mode=I2S.RX,
    bits=BITS,
    format=CHANNELS,
    rate=SAMPLE_RATE,
    ibuf=BUFFER_SIZE
)

buffer = bytearray(BUFFER_SIZE)
data = [[0 for i in range(BUFFER_SAMPLES)] for j in range(CHANNELS+1)]

try:
    while True:
        count = bus.readinto(buffer)
        if count > 0:
            
            # Convert buffer to big endian 16-bit integers
            for i in range(0, count, DATA_SIZE):
                j = i//DATA_SIZE%(CHANNELS+1)
                k = i//DATA_SIZE//(CHANNELS+1)
                data[j][k] = struct.unpack_from(FORMAT, buffer, i)[0]
            
            # Calculate level of each channel
            ac_min = [0 for i in range(CHANNELS+1)]
            ac_max = [0 for i in range(CHANNELS+1)]
            ac_lvl = [0 for i in range(CHANNELS+1)]
            for i in range(CHANNELS+1):
                for j in range(BUFFER_SAMPLES):
                    if data[i][j] > ac_max[i]:
                        ac_max[i] = data[i][j]
                    elif data[i][j] < ac_min[i]:
                        ac_min[i] = data[i][j]
                ac_lvl[i] = abs(ac_max[i] - ac_min[i])
            print(",".join(str(i) for i in ac_lvl))
            
except (KeyboardInterrupt, Exception) as e:
    print("{}: {}".format(type(e).__name__, e))

bus.deinit()
