from machine import Pin
from time import sleep

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ssid', 'password')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()

import urequests

sunny = Pin(12, Pin.OUT)
cloudy = Pin(13, Pin.OUT)
rainy = Pin(14, Pin.OUT)

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
