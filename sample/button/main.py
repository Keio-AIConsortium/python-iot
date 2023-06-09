from machine import Pin
from time import sleep

button = Pin(10, Pin.IN)

while True:
    print(f'Pin 10 is {button.value()}')
    sleep(0.1)
