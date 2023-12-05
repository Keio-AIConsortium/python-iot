from machine import Pin, PWM
from time import sleep

pin = Pin(Pin.board.GP20, Pin.OUT)
servo = PWM(pin)
servo.freq(50)


def servo_angle(angle):
    servo.duty_ns(int((angle / 180 * (2400 - 500) + 500) * 1000))


while True:
    servo_angle(0)
    sleep(1)
    servo_angle(90)
    sleep(1)
    servo_angle(180)
    sleep(1)
