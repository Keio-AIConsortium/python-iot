from machine import Pin
import time

trig = Pin(2, Pin.OUT)
echo = Pin(4, Pin.IN)

while True:
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    while echo.value() == 0:
        pass
    
    
    start_time = time.ticks_us()
    prev_echo = 0
    
    while time.ticks_us() - start_time < 60000:
        echo_state = echo.value()
        
        
        if prev_echo and not echo_state:
            echo_time = time.ticks_us() - start_time
            dist = echo_time * 340.0 * 1e-3 / 2
            print(f"echo: {echo_time} us, dist: {dist} mm")
            prev_echo = 0
            break
        
        prev_echo  = echo_state
        
    if prev_echo:
        print("over range")
        
    time.sleep_ms(60)
        
    
    