from machine import Pin, PWM
import time

pwm_led = PWM(Pin(18,mode=Pin.OUT))
pmw_led.freq(1_000)
pwm_led.duty_u16(13000)

while True:
    for light in range(1000, 30000, 1000):
        pmw_led.duty_u16(light)
        time.sleep(0,05)
    for light in range (30000, 950, -1000):
        pmw_led.duty_u16(light)
        time.sleep(0,05)
    