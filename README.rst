pico_synth_sandbox Hardware
===========================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
    :target: https://www.gnu.org/licenses/gpl-3.0
    :alt: GPL v3 License

Raspberry Pi Pico digital synthesizer board with I2S or PWM audio, a PDM microphone, MIDI i/o, a capacitive keybed, 1602 display, a rotary encoder, and LiPo battery. Designed for use with CircuitPython and synthio.

.. list-table::

    * - .. image:: _static/front-side.jpg
            :alt: Front view of 3d rendered board
      - .. image:: _static/back-side.jpg
            :alt: Back view of 3d rendered board
      - .. image:: _static/bottom.jpg
            :alt: Bottom view of 3d rendered board

Features
--------

* PCM5102 I2S DAC module compatibility or with populated components
* Optional PWM audio output
* LiPo Battery usb charging and power supply controlled by 3v3_enable
* MIDI input and output via MIDI TRS-A 3.5mm jack (compatible with most adapters)
* Dedicated volume pot with on-board speaker and line output
* 12 capacitive sense touch buttons serving as a single-octave keybed
* Software reset button
* 1602 display and rotary encoder with switch
* Optional PDM Microphone

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
      - Function

    * - GP0
      - Encoder A (included in UART0 header)
    * - GP1
      - Encoder B (included in UART0 header)
    * - GP2
      - Encoder Switch
    * - GP3
      - Touch Pad 2 (C#)
    * - GP4
      - MIDITX (UART1) or Microphone PDM Clock (JP2)
    * - GP5
      - MIDIRX (UART1) or Microphone PDM Data (JP1)
    * - GP6
      - Touch Pad 3 (D)
    * - GP7
      - Touch Pad 4 (D#)
    * - GP8
      - Touch Pad 5 (E)
    * - GP9
      - Touch Pad 6 (F)
    * - GP10
      - Touch Pad 7 (F#)
    * - GP11
      - Touch Pad 8 (G)
    * - GP12
      - Touch Pad 9 (G#)
    * - GP13
      - Touch Pad 10 (A)
    * - GP14
      - Touch Pad 11 (A#)
    * - GP15
      - Touch Pad 12 (B)
    * - GP16
      - I2S Clock or Left PWM (JP3/JP5)
    * - GP17
      - I2S Word (LR) Select or Right PWM (JP4/JP6)
    * - GP18
      - I2S Data
    * - GP19
      - Touch Pad 1 (C)
    * - GP20
      - 1602 Reset
    * - GP21
      - 1602 Enable
    * - GP22
      - 1602 D4
    * - GP26
      - 1602 D5
    * - GP27
      - 1602 D6
    * - GP28
      - 1602 D7

Schematic
---------

.. image:: _static/schematic.jpg
   :alt: Hardware schematic of pico_synth_sandbox device
   :target: _static/pico_synth_sandbox-schematic.pdf

Attribution
-----------

* Project inspired by `todbot/pico_test_synth <https://github.com/todbot/pico_test_synth>`_
