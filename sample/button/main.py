from machine import Pin
from time import sleep

button = Pin(Pin.board.GP15, Pin.IN, Pin.PULL_UP)

while True:
    print(f'Pin GP15 is {button.value()}')
    sleep(0.1)
