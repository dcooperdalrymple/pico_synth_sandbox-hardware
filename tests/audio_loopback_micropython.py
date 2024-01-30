from machine import Pin
from machine import I2S
import uasyncio as asyncio
import struct

BUFFER_SIZE = 8192
BITS = 16
SAMPLE_RATE = 22050
CHANNELS = I2S.STEREO

bus_input = I2S(
    0, # Bus ID
    sck=Pin(8),
    ws=Pin(9),
    sd=Pin(10),
    mode=I2S.RX,
    bits=BITS,
    format=CHANNELS,
    rate=SAMPLE_RATE,
    ibuf=BUFFER_SIZE*2
)

bus_output = I2S(
    1, # Bus ID
    sck=Pin(19),
    ws=Pin(20),
    sd=Pin(21),
    mode=I2S.TX,
    bits=BITS,
    format=CHANNELS,
    rate=SAMPLE_RATE,
    ibuf=BUFFER_SIZE*2
)

count = [0, 0]
buffer_read_index = 0
buffer_write_index = 0
buffers = [memoryview(bytearray(BUFFER_SIZE)), memoryview(bytearray(BUFFER_SIZE))]

def convert(buffer, length, in_fmt, out_fmt):
    if struct.calcsize(in_fmt) != struct.calcsize(out_fmt): return
    # NOTE: This operation is slow at the moment
    for i in range(0, length, struct.calcsize(in_fmt)):
        struct.pack_into(out_fmt, buffer, i, struct.unpack_from(in_fmt, buffer, i)[0])

async def read_buffer():
    global bus_input, count, buffer_read_index, buffer_write_index, buffers
    sreader = asyncio.StreamReader(bus_input)
    while True:
        # Read into buffer
        count[buffer_read_index] = await sreader.readinto(buffers[buffer_read_index])
        if count[buffer_read_index] > 0:
            # Increment buffer index
            buffer_read_index = (buffer_read_index + 1) % 2
            # Wait for write to be ready
            while buffer_read_index == buffer_write_index:
                await asyncio.sleep_ms(1)

async def write_buffer():
    global bus_output, count, buffer_write_index, buffer_read_index, buffers
    swriter = asyncio.StreamWriter(bus_output)
    while True:
        # Wait for read to be ready
        while buffer_write_index == buffer_read_index:
            await asyncio.sleep_ms(1)
        # Convert from big endian to little endian
        convert(buffers[buffer_write_index], count[buffer_write_index], ">h", "<h")
        # Write into buffer
        swriter.out_buf = buffers[buffer_write_index][:count[buffer_write_index]]
        await swriter.drain()
        # Increment buffer index
        buffer_write_index = (buffer_write_index + 1) % 2

async def main():
    asyncio.create_task(read_buffer())
    asyncio.create_task(write_buffer())
    while True:
        await asyncio.sleep_ms(10)

try:
    asyncio.run(main())
except (KeyboardInterrupt, Exception) as e:
    print("{}: {}".format(type(e).__name__, e))
finally:
    bus_input.deinit()
    bus_output.deinit()
    asyncio.new_event_loop()
