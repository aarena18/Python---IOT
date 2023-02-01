from machine import Pin
import utime

print('ok')


pinNumber = 17
led = Pin(pinNumber, mode=Pin.OUT)

while True:
    led.toggle()
    utime.sleep(0.1)
    
    