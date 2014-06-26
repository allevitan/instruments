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
	#your shitty code goes here
```

This syntax ensures that the connection to the instrument is safely closed, regardless of any exceptions thrown by your shitty code.

_Voltmeter_, _Ammeter_, _Encoder_, _SerialInstrument_, and _GPIBInstrument_ implement the `instr.read(num=None)` method, which reads _num_ values from the instrument. If _num_ is not provided, it will read a single value.

_Oscilloscope_ is fundamentally different - calling `scope.read(channels)` will return current data from each channel in _channels_.

## Installation of dependencies

* Install [anaconda python](https://store.continuum.io/cshop/anaconda/).
* Install [NI-VISA](http://www.ni.com/visa/), [TEKVISA](https://www.google.com/#q=tekvisa), or some other VISA library. Note that while NI-VISA is the best, installing it is a huge pain in the butt.
* run `pip install pyserial pyvisa` from the terminal (OSX/Linux) or cmd.exe (Windows).

## Questions
Email me at allevitan@gmail.com if something is unclear and fork the repo if you want to make it better!
