from machine import Pin
from time import sleep
from esp_config import *

led = Pin(D1, Pin.OUT)
button = Pin(D2, Pin.IN)

while True:
    if button.value():
        led.value(0)
    else:
        led.value(1)

# 例2
    # if not button.value():
    #     led.value(1)
    # else:
    #     led.value(0)
        
# 例3
#    led.value(not button.value())
        
    sleep(0.1)