# This file is executed on every boot (including wake-boot from deepsleep)
try:
  import usocket as socket
except:
  import socket
  
import network
import time
import esp
esp.osdebug(None)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

from machine import Pin, SoftI2C, UART
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

# ESP8266 Pin assignment
#i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Uncomment the below to connect to Wifi
#station = network.WLAN(network.STA_IF)

#station.active(True)
#station.connect('wifi_name', 'pwd')
# while station.isconnected() == False:
#   pass
# 
# print('Connection successful')
# print(station.ifconfig())

# Activating soft access point
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
print(ap_if.ifconfig())

led = Pin(2, Pin.OUT)

oled.text('LOVE', 0, 0)
oled.text('LOVE', 0, 20)
oled.text('LOVE MY SWEETIE', 0, 30)
oled.text('HOTTIE PIE', 0, 40)
oled.text('Sleep for 5sec', 0, 50)
        
oled.show()
sleep(5)

