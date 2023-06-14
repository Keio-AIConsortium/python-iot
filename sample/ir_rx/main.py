import time
from machine import Pin
from ir_rx import NEC_8
from esp_config import *

def callback(data, addr, ctrl):
    if data < 0:
        print('Repeat code.')

    else:
        print('Data {:02X} Addr {:04x}'.format(data, addr))

ir = NEC_8(Pin(D7, Pin.IN), callback)

while True:
    time.sleep_ms(500)
