from machine import Pin, I2C
from lcd import Lcd
from time import sleep

lcd = Lcd(I2C(0, scl=Pin.board.GP1, sda=Pin.board.GP0))

while True:
    lcd.print("Hello, world!")
    for i in range(100):
        lcd.move_to(0, 1)
        lcd.print(str(i))
        sleep(1)
    lcd.clear()
    sleep(1)
