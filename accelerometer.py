from machine import I2C, Pin
import mpu6050
i2c = I2C(scl=Pin(5), sda=Pin(4))
accelerometer = mpu6050.accel(i2c)

from time import sleep
while True:
    sleep(2)
    print(accelerometer.get_values())
    print('/n')
#{'GyZ': -235, 'GyY': 296, 'GyX': 16, 'Tmp': 26.64764, 'AcZ': -1552, 'AcY': -412, 'AcX': 16892}
