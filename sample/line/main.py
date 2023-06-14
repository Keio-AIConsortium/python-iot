import urequests
import ujson
from wifi import connect
from urllib import parse

if __name__ == "__main__":
    connect()
    token = ''
    msg='こんにちは！ PythonではじめるIoT'
    
    res = urequests.post(
        'https://notify-api.line.me/api/notify',
        data = 'message='+parse(msg),
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + token
        }
    )

    print (res.json())
    res.close()

