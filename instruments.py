from __future__ import print_function, division
import numpy as np
import visa
from serial import Serial

#
#Basic Types of Instruments
#

class GPIBInstrument(object):
    
    def __init__(self, gpib_id):
        self.gpib_id = gpib_id

    def read(self, num=None):
        if num:
            return [float(self.instr.read())
                    for i in range(0, num)]
        return float(self.instr.read())

    def write(self, data):
        self.instr.write(data)

    def __enter__(self):
        self.instr = visa.instrument("GPIB::{0}".format(self.gpib_id))
        self.instr.write('G1')
        self.instr.write('X')
        return self

    def __exit__(self, type, value, tb):
        self.instr.close()
        self.instr = None


class SerialInstrument(object):

    def __init__(self, port, baud=19200):
        self.port = port
        self.baud = baud

    def read(self, num=None):
        if num:
            while self.instr.inWaiting() < num:
                pass
            return self.instr.read(num)
        while not self.instr.inWaiting():
            pass
        return self.instr.read()
        
    def write(self, data):
        self.instr.write(data)

    def __enter__(self):
        self.instr = Serial(self.port, self.baud)
        self.instr.open()
        return self

    def __exit__(self, type, value, tb):
        self.instr.close()

            
#
#Specific classes made to work with instruments in the lab
#

class Voltmeter(GPIBInstrument):
    #Juat to make the end code clearer
    pass

class Ammeter(GPIBInstrument):
    #Just to make the end code clearer
    pass


class Oscilloscope(object):

    def __init__(self, loc='USB0::0x0699::0x0368::C020288::INSTR'):
        self.loc = loc;
    
    def __enter__():
        self.scope = visa.instrument(loc)
    
    def __exit__():
        self.scope.close()

    def read(self,channels):
        output = {}
        xincr = float(scope.ask('WFMPRE:XINCR?'))
        
        for channel in channels:
            self.scope.write('DATA:SOU CH' + str(channel))
            self.scope.write('DATA:WIDTH 1')
            self.scope.write('DATA:ENC RPB')
            
            ymult = float(self.scope.ask('WFMPRE:YMULT?'))
            yzero = float(self.scope.ask('WFMPRE:YZERO?'))
            yoff = float(self.scope.ask('WFMPRE:YOFF?'))
            
            
            self.scope.write('CURVE?')
            data = self.scope.read_raw()
            headerlen = 2 + int(data[1])
            header = data[:headerlen]
            ADC_wave = data[headerlen:-1]
            
            ADC_wave = np.array(unpack('%sB' % len(ADC_wave),ADC_wave))
            
            output[channel] = (ADC_wave - yoff) * ymult  + yzero
            length = len(ADC_wave)
            
        output['time'] = np.arange(0, xincr * length, xincr)
        return output


class Encoder(SerialInstrument):
    
    def process_raw(self, raw):
        #If we've clearly mistook the high bit for the low bit
        if any(logical_and(raw[::2] > 15, raw[::2] < 240)):
            raw = hstack((raw[1:],list(self.read())))
            
        unsigned = 256 * raw[::2] + raw[1::2]
        signer = vectorize(lambda x: x if x <= 32767 else x - 65536)
        signed = signer(unsigned)

        #return an answer in radians
        return signed / 1440 * 2 * pi + theta0 * 180 / pi

    def read(self, num=None):
        if num:
            return self.process_raw(super(Encoder, self).read(num * 2))
        else:
            return self.process_raw(super(Encoder, self).read(2))[0]


class Heater(SerialInstrument):
    
    def on(self):
        self.write(bytearray([1])
    
    def off(self):
        self.write(bytearray([2]))
