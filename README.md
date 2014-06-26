# Instruments

Instruments is a set of classes that provide a consistent API to the instruments in Wellesley's 310 physics lab.

## Dependencies

* python 2 or 3
* numpy
* A standard VISA library (NI-VISA, TEKVISA, etc.)
* pyVISA
* pySerial

## Usage

Each instrument class is designed to be used in the following manner:

```python
from instruments import Voltmeter
with Voltmeter('COM3') as instr:
	print(instr.read(20))
	#your shitty code goes here
```

Which ensures that the connection is safely, regardless of any exceptions thrown by your shitty code.

Most instruments (_Voltmeter_, _Ammeter_, _Encoder_, _SerialInstrument_, and _GPIBInstrument_) implement:
__instr.read(num=None)__, which will read _num_ values from the instrument if _num_ is provided, or return a single value if called without an argument

The oscilloscope is fundamentally different from the other devices:
__scope.read(channels)__ will return the current data from each channel in the list.

## Installation of dependencies

* Install [anaconda python](https://store.continuum.io/cshop/anaconda/) or your favorite python distribution.
* Install [NI-VISA](http://www.ni.com/visa/), [TEKVISA](https://www.google.com/#q=tekvisa), or some other VISA library. Note that while NI-VISA is the best, installing it is a huge pain in the butt.
* From cmd.exe (windows) or the terminal (linux/osx) run `pip install pyserial pyvisa`. If you're not using anaconda python (which comes with numpy), make sure to install numpy now as well.

## Questions
Email me at allevitan@gmail.com if something is unclear, and/or fork the code if you want to make it better!
