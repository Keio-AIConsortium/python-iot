import urequests
import ujson
from wifi import connect

if __name__ == "__main__":
    connect()
    url = 'https://script.google.com/macros/s/AKfycbykWG7iPQOtfUZPqtg_whb8BiBX6EyC_j3xBrrTgM2jmj04ACsgGFOLyBLXOwHOaUIx/exec'
    data = {"api_key": "YOUR API KEY",
            "prompt": "What is your GPT model?"}
    res = urequests.post(url,
                         data=ujson.dumps(data).encode("utf-8"))

    print(res.text)
    res.close()
