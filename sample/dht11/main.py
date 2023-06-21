from esp_config import *
from time import sleep
import dht

d = dht.DHT11(machine.Pin(D6))
while True:
    d.measure()
    print('temp: ', d.temperature(), 'humidity: ', d.humidity())
    sleep(1)
