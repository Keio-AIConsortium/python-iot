import urequests
import ujson
from wifi import connect
    
if __name__ == "__main__":
    connect()
    url = ''
    data = {"temperature" : "23.4", "humidity" : "50"}
    res = urequests.post(
        url,
        data = ujson.dumps(data).encode("utf-8"),
        headers = {'Content-Type' : 'application/json'}
    )

    print (res.json())
    res.close()
