from machine import Pin
from time import sleep
from esp_config import *

button = Pin(5, Pin.IN)

while True:
    print(f'Pin 10 is {button.value()}')
    sleep(0.1)

