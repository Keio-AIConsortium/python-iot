from time import sleep
from machine import Pin
from ir_rx import NEC_8


def callback(data, addr, ctrl):
    if data < 0:
        print('Repeat code.')

    else:
        print('Data {:02X} Addr {:04x}'.format(data, addr))


ir = NEC_8(Pin(Pin.board.GP10, Pin.IN), callback)

while True:
    sleep(0.5)
