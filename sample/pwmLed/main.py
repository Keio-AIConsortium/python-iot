from machine import Pin, PWM
from time import sleep

led = Pin(Pin.board.GP18, Pin.OUT)
pwm = PWM(led)

while True:
    pwm.duty_u16(65535)
    sleep(1)
    pwm.duty_u16(10000)
    sleep(1)
    pwm.duty_u16(0)
    sleep(1)
