from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
#i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('LOVE', 0, 0)
oled.text('LOVE', 0, 20)
oled.text('LOVE MY SWEETIE', 0, 40)
oled.text('HOTTIE PIE', 0, 50)
        
oled.show()
