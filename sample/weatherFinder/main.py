from machine import Pin
from time import sleep
from esp_config import *
from wifi import connect

import urequests

sunny = Pin(D6, Pin.OUT)
cloudy = Pin(D7, Pin.OUT)
rainy = Pin(D5, Pin.OUT)
connect()
while True:
    r = urequests.get('https://weather.tsukumijima.net/api/forecast?city=140010')
    j = r.json()
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
