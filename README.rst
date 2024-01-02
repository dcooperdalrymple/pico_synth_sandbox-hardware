pico_synth_sandbox Hardware
===========================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0
    :alt: GPL v3 License

Raspberry Pi Pico digital synthesizer board with stereo I2S audio (ADC & DAC), stereo omnidirectional MEMS microphones, MIDI i/o, a 16-key capacitive keybed, 1602 display, 2 rotary encoders, and LiPo battery charging and power distribution. Designed for use with CircuitPython and synthio.

.. list-table::

    * - .. image:: _static/front-side.jpg
            :alt: Front view of 3d rendered board
      - .. image:: _static/back-side.jpg
            :alt: Back view of 3d rendered board
      - .. image:: _static/bottom.jpg
            :alt: Bottom view of 3d rendered board

Features
--------

* PCM5102 I2S DAC with line output
* PCM1860 I2S ADC with line and microphone input
* PAM8019 amplifier with stereo class AB headphone and class D speaker output
* LiPo Battery usb charging and power supply controlled by 3v3_enable
* MIDI input and output via MIDI TRS-A 3.5mm jacks (compatible with most adapters)
* Input level potentiometer (line input only)
* Amplifier volume potentiometer (line output not included)
* 16 capacitive sense touch buttons powered by the TTP229-BSF
* 16x2 LCD character display
* 2 rotary encoders with push switches
* Micro SD card storage

Software
--------

CircuitPython Library
~~~~~~~~~~~~~~~~~~~~~

The pico_synth_sandbox is designed for use with CircuitPython and synthio. A specialized library with hardware abstraction and a multitude of additional features for embedded audio synthesis is available in the `pico_synth_sandbox <https://github.com/dcooperdalrymple/pico_synth_sandbox>`_ repository. Library documentation and other resources are available on `Read the Docs <https://pico-synth-sandbox.readthedocs.io/>`_.

CircuitPython Tests
~~~~~~~~~~~~~~~~~~~

A number of hardware tests are available within the ``./tests`` directory to validate the ``pico_synth_sandbox`` hardware using the REPL serial terminal.

RP2040 Pin Assignment
---------------------

Some pins require solder jumper configuration if you do not use the default pin assignment for MIDI & I2S.

.. list-table::
    :header-rows: 1

    * - Pin Reference
      - Assignment
      - Direction
      - Function

    * - GP0
      - SD Card RX
      - Input
      - SPI0
    * - GP1
      - SD Card CS
      - Output
      - SPI0
    * - GP2
      - SD Card SCK
      - Output
      - SPI0
    * - GP3
      - SD Card TX
      - Output
      - SPI0
    * - GP4
      - MIDITX
      - Output
      - UART1
    * - GP5
      - MIDIRX
      - Input
      - UART1
    * - GP6
      - 1602 Enable
      - Output
      - GPIO
    * - GP7
      - 1602 Reset
      - Output
      - GPIO
    * - GP8
      - ADC Serial Clock
      - Output
      - I2S
    * - GP9
      - ADC Word Select
      - Output
      - I2S
    * - GP10
      - ADC Serial Data
      - Input
      - I2S
    * - GP11
      - Encoder 1 A
      - Input
      - GPIO
    * - GP12
      - Encoder 1 B
      - Input
      - GPIO
    * - GP13
      - Encoder 1 Switch
      - Input
      - GPIO
    * - GP14
      - TTP229 Serial Data
      - Input
      - GPIO
    * - GP15
      - TTP229 Serial Clock
      - Output
      - GPIO
    * - GP16
      - Encoder 2 A
      - Input
      - GPIO
    * - GP17
      - Encoder 2 B
      - Input
      - GPIO
    * - GP18
      - Encoder 2 Switch
      - Input
      - GPIO
    * - GP19
      - DAC Serial Clock
      - Output
      - I2S
    * - GP20
      - DAC Word Select
      - Output
      - I2S
    * - GP21
      - DAC Serial Data
      - Output
      - I2S
    * - GP22
      - 1602 D7
      - Output
      - GPIO
    * - GP26
      - 1602 D6
      - Output
      - GPIO
    * - GP27
      - 1602 D5
      - Output
      - GPIO
    * - GP28
      - 1602 D4
      - Output
      - GPIO

Schematic
---------

.. image:: _static/schematic.jpg
   :alt: Hardware schematic of pico_synth_sandbox device
   :target: _static/schematic.pdf

Attribution
-----------

* Project inspired by `todbot/pico_test_synth <https://github.com/todbot/pico_test_synth>`_
