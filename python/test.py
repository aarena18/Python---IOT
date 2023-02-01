from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time

WIDTH = 128
HEIGHT = 64

i2c = I2C (0, scl = Pin (17), sda = Pin(16), freq=400000)

display = SSD1306_I2C(WIDTH, HEIGHT, i2c)
display.rotate(1)
display.fill(0)
display.text("salut",0,14)
display.show()
#display.fill(0)