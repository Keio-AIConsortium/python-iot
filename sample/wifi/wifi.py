import urequests

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('SSID', 'PASS')
            pass
    print('network config:', sta_if.ifconfig())


do_connect()
r = urequests.get('https://weather.tsukumijima.net/api/forecast/city/400040')
print(r)
