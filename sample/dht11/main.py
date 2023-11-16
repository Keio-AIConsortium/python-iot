from time import sleep
from machine import Pin
import dht

d = dht.DHT11(Pin(Pin.board.GP15))
while True:
    d.measure()
    print('temp: ', d.temperature(), 'humidity: ', d.humidity())
    sleep(1)
