import urequests
import ujson
from wifi import connect

if __name__ == "__main__":
    connect()
    ACCESS_TOKEN = "YOUR ACCESS TOKEN"
    message = "hello, world"

    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer " + ACCESS_TOKEN,
    }
    payload = {
        "messages": [
            {
                "type": "text",
                "text": message,
            }
        ],
        "notificationDisabled": False,
    }
    res = urequests.post(url, headers=headers, data=ujson.dumps(payload).encode("utf-8"))
    print(res.text)
    res.close()
