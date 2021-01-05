
import serial
import io
import time

class Rotronic:
    def __init__(self,port='COM31',baud_rate=19200,bits=8,parity=serial.PARITY_NONE):
        #communication
        self.port=port
        self.baud_rate=baud_rate
        self.bits=bits
        self.parity=parity
        self.interface=serial.Serial(self.port, self.baud_rate, self.bits,self.parity)
        self.delay=0.5

        self.temperature=None
        self.humidity=None
        self.serial_number=None
        self.reading_command=b'{F00RDD}\r'

    def get_reading(self,verbose=False):
        self.interface.write(self.reading_command)
        time.sleep(self.delay)
        buffer=self.interface.read_all()
        while(len(buffer)<4):
            buffer = self.interface.read_all()
        buffer=str(buffer).split(";")
        self.humidity=buffer[1]
        self.temperature=buffer[5]
        self.serial_number=buffer[16]
        if verbose:
            print(f'T={self.temperature}, rh={self.humidity}')
        return self.temperature,self.humidity,self.serial_number

    def get_temp(self,verbose=False):
        self.temperature=self.get_reading()[0]
        if verbose:
            print(f'T={self.temperature}')
        return self.temperature

    def get_humidity(self,verbose=False):
        self.humidity=self.get_reading()[1]
        if verbose:
            print(f'rh={self.humidity}')
        return self.humidity

    def get_serial_number(self,verbose=False):
        self.serial_number=self.get_reading()[2]
        if verbose:
            print(f'rh={self.serial_number}')
        return self.serial_number

    def close(self):
        self.interface.close()

def
