from esp_config import *
from time import sleep
import dht

d = dht.DHT11(machine.Pin(D5))
while True:
    d.measure()
    print(d.temperature())
    print(d.humidity())
    sleep(1)
