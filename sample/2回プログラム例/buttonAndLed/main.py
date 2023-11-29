from machine import Pin
from time import sleep

led = Pin(Pin.board.GP18, Pin.OUT)
button = Pin(Pin.board.GP15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value():
        led.value(0)
    else:
        led.value(1)

    sleep(0.1)
# 例2
"""     if not button.value():
        led.value(1)
    else:
        led.value(0)
 """
# 例3
# led.value(not button.value())
