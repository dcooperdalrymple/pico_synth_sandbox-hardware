import audiocore
import audiobusio
import board
import array
import time
import math

sample_rate = 22050
length = sample_rate // 440
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / length) * (2 ** 15) + 2 ** 15)
sine_wave = audiocore.RawSample(sine_wave, sample_rate=sample_rate)

dac = audiobusio.I2SOut(
    bit_clock=board.GP19,
    word_select=board.GP20,
    data=board.GP21
)

while True:
    dac.play(sine_wave, loop=True)
    time.sleep(0.5)
    dac.stop()
    time.sleep(0.5)
