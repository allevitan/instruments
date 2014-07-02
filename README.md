# Instruments

Instruments is a (fairly) consistent python interface for the instruments in Wellesley's 310 physics lab.

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
	#your code goes here
```

This syntax ensures that the connection to the instrument will be safely closed, regardless of any exceptions thrown by your code.

_Voltmeter_, _Ammeter_, _Encoder_, _SerialInstrument_, and _GPIBInstrument_ implement the `instr.read(num)` method, which reads _num_ values from the instrument. If _num_ is not provided, it will read a single value.

_Oscilloscope_ is fundamentally different - calling `scope.read(channels)` will return current data from each channel in _channels_.

_Heater_, the heater for the heat capacity of copper lab, is also different. It has two methods, `heater.on()` and `heater.off()` which do exactly what you'd expect.

## Examples

* Print the next 100 readings from an ammeter:
```python
from instruments import Ammeter

with Ammeter(6) as amp: #ammeter on GPIB bus 6
	print(amp.read(100))
```
* Plot channels 1 and 3 from an oscilloscope:
```python
from instruments import Oscilloscope
from matplotlib.pyplot import *

with Oscilloscope() as scope:
	data = scope.read([1,3])

plot(data['time'],data[1])
plot(data['time'],data[3])
show()
```

## Installation of dependencies

* Install [anaconda python](https://store.continuum.io/cshop/anaconda/).
* Install [NI-VISA](http://www.ni.com/visa/), [TEKVISA](https://www.google.com/#q=tekvisa), or some other VISA library. Note that while NI-VISA is the best, installing it is a huge pain in the butt.
* Run `pip install pyserial pyvisa` from the terminal (OSX/Linux) or cmd.exe (Windows).

## Questions
Email me at allevitan@gmail.com if something is unclear and fork the repo if you want to make it better!
