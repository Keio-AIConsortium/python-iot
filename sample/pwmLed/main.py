from machine import Pin, PWM
from time import sleep
from esp_config import *

led = Pin(D2, Pin.OUT)
pwm = PWM(led)

while True:
    pwm.duty(1023)
    sleep(1)
    pwm.duty(512)
    sleep(1)
    pwm.duty(0)
    sleep(1)
    
