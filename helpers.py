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

def dev_disp(txts):
    '''
    txts is a list of strings
    '''
    oled.fill(0)
    oled.show()
    sleep(0.5)
    
    if len(txts)>5:
        txts = txts[:5]
    
    for i, txt in enumerate(txts):
        oled.text(txt, 0, i*10)
    
    oled.show()
