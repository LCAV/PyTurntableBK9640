Bruel & Kjaer Turntable System Driver
=====================================

This is a simple python driver for the B&K Turntable System Type 9640 using the
[PyVISA](http://pyvisa.readthedocs.io/en/stable/index.html) module, itself a
wrapper around the NI-VISA library (available for
[windows](http://www.ni.com/download/ni-visa-5.4.1/4626/en/),
[linux](http://www.ni.com/download/ni-visa-5.4.1/4629/en/), and
[mac](http://www.ni.com/download/ni-visa-14.0.2/5075/en/)).

As of now, only absolute positioning has been implemented.

Installation
------------

First, the NI-VISA library should be [download]() and installed. Instructions
are available in the PyVISA [documentation](http://pyvisa.readthedocs.io/en/stable/getting_nivisa.html).

Second, the PyVISA library can be installed from `pip` directly.

    pip install -U pyvisa

Quick Start
-----------

This is a simple example of setting the turntable in some absolute direction.
First, the instrument name can be printed using the convenience function `turntable.list_instruments()`.

    > import turntable
    > print(turntable.list_instruments())
    ('ASRL1::INSTR','ASRL2::INSTR','ASRL3::INSTR')

Knowing the name, the turntable is controlled in the following way (assuming the third instrument is the one we need).
Here the table is turned the direction at 37 degrees.

    > import turntable
    > table = turntable.TurnTable('ASRL3::INSTR')
    > table.turn_abs(37)

The zero location of the table can be set to the current location by typing

    > table.set_zero()

License
-------

Copyright 2017 Robin Scheibler

    /*
     * ----------------------------------------------------------------------------
     * "THE BEER-WARE LICENSE" (Revision 42):
     * <fakufaku@gmail.com> wrote this file.  As long as you retain this notice you
     * can do whatever you want with this stuff. If we meet some day, and you think
     * this stuff is worth it, you can buy me a beer in return.     Robin Scheibler
     * ----------------------------------------------------------------------------
     */
