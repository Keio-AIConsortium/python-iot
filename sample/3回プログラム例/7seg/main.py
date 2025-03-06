from machine import Pin, RTC
import tm1637
import utime
import time

seg = tm1637.TM1637(clk=Pin.board.GP0, dio=Pin.board.GP1) # clock display
rtc = RTC()

# 時刻を取得する関数
def get_jst():
    tm = utime.localtime(utime.time())  # UTC now
    time = ('0'+str(tm[3]))[-2:] + ('0'+str(tm[4]))[-2:]  # JST now
    return time

while True:
    # 現在時刻を表示
    seg.show(get_jst())
    time.sleep(1)
    
