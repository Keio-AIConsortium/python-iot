import urequests
import ujson
import wifi
from time import sleep
from machine import Pin
import dht
d = dht.DHT11(Pin(Pin.board.GP15))

if __name__ == "__main__":
    wifi.do_connect()
    url = 'URLを入力'
    d.measure()
    data = {"temperature": d.temperature(), "humidity": d.humidity()}
    res = urequests.post(url,
                         data=ujson.dumps(data).encode("utf-8"),
                         headers={'Content-Type': 'application/json'})

    print(res.json())
    res.close()
