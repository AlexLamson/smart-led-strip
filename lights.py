from time import sleep
import numpy as np
import sys
import serial.tools.list_ports
import serial

# connect to the open serial port
ports = list(serial.tools.list_ports.comports())
ports = [p[0] for p in ports]
if len(ports) == 0:
    print("couldn't find any open ports")
    exit()
ser = serial.Serial(ports[0], 115200, timeout=0.5)

NUM_LEDS = 226

output = bytearray([0]+[255 for _ in range(NUM_LEDS)])
ser.write(output)
output = bytearray([1]+[255 for _ in range(NUM_LEDS)])
ser.write(output)
output = bytearray([2]+[255 for _ in range(NUM_LEDS)])
ser.write(output)

