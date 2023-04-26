from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(18, Pin.OUT), sda=Pin(19, Pin.OUT),
          freq=400000)

print(i2c)

oled = SSD1306_I2C(128, 64, i2c)
oled.init_display()

oled.fill(0xff0000)
oled.text("Python IoT", 0, 40, 0)
oled.show()

