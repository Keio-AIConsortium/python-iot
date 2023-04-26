from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(4, Pin.OUT))
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
