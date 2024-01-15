try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import time
import esp
esp.osdebug(None)

import gc
gc.collect()

from machine import I2C, Pin
import mpu6050

i2c = I2C(scl=Pin(5), sda=Pin(4))
accelerometer = mpu6050.accel(i2c)

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect('RedPanda_2.4', 'merryweather246')

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)


