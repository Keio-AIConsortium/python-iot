from machine import Pin
from time import sleep

led = Pin(16, Pin.OUT)
button = Pin(10, Pin.IN)

while True:
# 例1
#     if button.value():
#         led.value(0)
#     else:
#         led.value(1)

# 例2
    if not button.value():
        led.value(1)
    else:
        led.value(0)
        
# 例3
#    led.value(not button.value())
        
    sleep(0.1)