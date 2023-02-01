from machine import Pin
import time

pinNumber = 17
pinNumberTwo = 18
pinNumberThree = 19

ledBlue = Pin(pinNumber, mode=Pin.OUT)
ledWhite = Pin(pinNumberTwo, mode=Pin.OUT)
ledRed = Pin(pinNumberThree, mode=Pin.OUT)

while True:
    ledBlue.toggle()
    time.sleep(1)
    ledWhite.toggle()
    time.sleep(1)
    ledRed.toggle()
    time.sleep(1)
    
    #led.on()
    #led.off()