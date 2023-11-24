from machine import Pin
from time import sleep
import urequests
import wifi

sunny = Pin(Pin.board.GP18, Pin.OUT)
cloudy = Pin(Pin.board.GP19, Pin.OUT)
rainy = Pin(Pin.board.GP20, Pin.OUT)

do_connect()

while True:
    r = urequests.get(
        'https://weather.tsukumijima.net/api/forecast?city=140010')
    j = r.json()
    print(j['forecasts'][1])
    tomorrow = j['forecasts'][1]['telop']

    if "雨" in tomorrow:
        sunny.value(0)
        cloudy.value(0)
        rainy.value(1)
        print("rainy")
    elif "曇" in tomorrow:
        sunny.value(0)
        cloudy.value(1)
        rainy.value(0)
        print("cloudy")
    else:
        sunny.value(1)
        cloudy.value(0)
        rainy.value(0)
        print("sunny")

    sleep(1000)
