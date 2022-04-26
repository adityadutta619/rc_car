from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import mpu6050

# ESP32 Pin assignment 
#i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

accelerometer = mpu6050.accel(i2c)

oled.text('LOVE', 0, 0)
oled.text('LOVE', 0, 20)
oled.text('LOVE MY SWEETIE', 0, 40)
oled.text('HOTTIE PIE', 0, 50)
        
oled.show()
sleep(3)

while True:
    oled.fill(0)
    oled.show()
    sleep(0.2)
    x = accelerometer.get_values()
    for i,j in enumerate(['GyZ', 'GyY', 'GyX', 'AcZ', 'AcY', 'AcX']):
        oled.text('{}: {}'.format(j, x[j]),0,i*10)
    oled.show()
    sleep(0.8)
        
        
        