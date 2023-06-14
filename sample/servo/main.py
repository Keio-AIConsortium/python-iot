from machine import Pin, PWM
from time import sleep
from esp_config import *

servo = PWM(Pin(D1, Pin.OUT))
servo.freq(50)


def servo_angle(angle):
    servo.duty((123 - 26) * angle / 180 + 26)


while True:
    servo_angle(0)
    sleep(1)
    servo_angle(90)
    sleep(1)
    servo_angle(180)
    sleep(1)
