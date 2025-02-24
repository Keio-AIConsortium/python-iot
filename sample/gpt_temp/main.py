from time import sleep

import dht
import ujson
import urequests
from machine import Pin, I2C
from lcd import Lcd

if __name__ == "__main__":
    d = dht.DHT11(Pin(Pin.board.GP15))
    i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)
    lcd = Lcd(i2c, i2c_addr=0x27)
    sleep(1)

    d.measure()
    print('temp: ', d.temperature(), 'humidity: ', d.humidity())
    sleep(1)

    url = 'https://script.google.com/macros/s/AKfycbykWG7iPQOtfUZPqtg_whb8BiBX6EyC_j3xBrrTgM2jmj04ACsgGFOLyBLXOwHOaUIx/exec'
    data = {
        "api_key":
        "<API_KEY>",
        "prompt":
        f"Celcius: {d.temperature()} Humidity: {d.humidity()}, 温度の情報を盛り込んだ挨拶を英語で 5 wordで言ってください"
    }
    res = urequests.post(url, data=ujson.dumps(data).encode("utf-8"))

    print(res.text)
    lcd.print(res.json()["response"])
  
