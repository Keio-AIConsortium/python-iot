from machine import Pin, ADC
from time import sleep
from esp_config import *

adc = ADC(0)

while True:
    print(adc.read())
    sleep(0.1)