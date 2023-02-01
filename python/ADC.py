from machine import Pin, ADC
import time

adc = ADC(Pin(28, mode=Pin.IN))
pwm_led = PWM(Pin(17,mode=Pin.OUT))
pwm_led.freq(1_000)

while True :
    val = adc.read_u16()
    val = val * (3.3 / 65535)
    print(round(val,2), "V")
    time.sleep_ms(100)
    
    
    
