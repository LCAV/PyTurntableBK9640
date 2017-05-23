'''
This is a simple python driver for the B&K Turntable System Type 9640 using the PyVISA
[1] module, itself a wrapper around the NI-VISA library (available for windows
[2], linux [3], and mac [4]).

As of now, only absolute positioning has been implemented.

Revision History
-----------------

2017/05 Robin Scheibler: initial creation of the file

References
----------

[1] http://pyvisa.readthedocs.io/en/stable/index.html
[2] http://www.ni.com/download/ni-visa-5.4.1/4626/en/
[3] http://www.ni.com/download/ni-visa-5.4.1/4629/en/
[4] http://www.ni.com/download/ni-visa-14.0.2/5075/en/

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

    ----------------------------------------------------------------------------
    "THE BEER-WARE LICENSE" (Revision 42):
    <fakufaku@gmail.com> wrote this file.  As long as you retain this notice you
    can do whatever you want with this stuff. If we meet some day, and you think
    this stuff is worth it, you can buy me a beer in return.     Robin Scheibler
    ----------------------------------------------------------------------------
'''

import visa

def list_instruments():
    ''' Shortcut to the list resources function '''
    rm = visa.ResourceManager()
    return rm.list_resources()

class TurnTable(object):
    '''
    This object can be used to control a Bruel & Kjaer turntable
    '''

    def __init__(self, device_name):
        '''
        Initialize the turntable.

        Parameters
        ----------
        device_name: str
            The device name should be the one provided by the function `turntable.list_instruments()`.
        '''

        self.rm = visa.ResourceManager()
        self.instrument = self.rm.open_resource(device_name)

        # initialization sequence
        self.instrument.write('++mode 1')
        self.instrument.write('++addr 10')
        self.instrument.write('++auto 0')

    def set_acc(self, acceleration):
        ''' Set the acceleration of the turntable '''
        self.instrument.write('Acc. {}'.format(acceleration))

    def turn_abs(self, angle):
        '''
        Set the absolute orientation of the turntable

        Parameters
        ----------
        angle: int
            The angle to set the turntable
        '''
        self.instrument.write('Max_360 on')
        self.instrument.write('Turn_abs {:3.0f}'.format(angle))
        self.instrument.write('Start')

    def set_zero(self):
        ''' Set the current position to be at zero degree '''
        self.instrument.write('Set 0 deg')

    def stop(self):
        ''' Stops the turntable '''
        self.instrument.write('Stop')
