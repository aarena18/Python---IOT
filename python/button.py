from machine import Pin
import utime

pin_button = Pin(16, mode=Pin.IN, pull=Pin.PULL_UP)

while True:
    print(pin_button.value())	# on renvoie la valeur du bouton 
    utime.sleep(1)				# on attend 0.1 sec