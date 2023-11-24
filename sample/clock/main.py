from machine import RTC
import utime
import ntptime
import wifi
from time import sleep

wifi.connect()
rtc = RTC()
ntptime.settime()  # setup time by remote NTP server


def get_jst():
    tm = utime.localtime(utime.time())  # UTC now
    jst = str(tm[0]) + '/' + str(tm[1]) + '/' + str(tm[2]) + ' ' + str(
        (tm[3] + 9) % 24) + ':' + str(tm[4]) + ':' + str(tm[5])
    return jst


while True:
    print(get_jst())
    sleep(1)
