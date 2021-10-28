# Change pins as needed

import machine
servo_pin = machine.Pin(14)
servo = machine.PWM(servo_pin, freq=50)

# Goes from 40 to 115
servo.duty(77)

motor_pin = machine.Pin(13)
#motor = machine.PWM(motor_pin, freq=50, duty=512)
motor = machine.PWM(motor_pin, freq=50)

while True:
# Arm the ESC******************

sleep(0.5) # give the ESC some time to warm up
motor.duty(90) #setting the duty cycle to 0
sleep(2)
break

for i in range(91, 115):
sleep(0.1) # give the ESC some time to warm up
motor.duty(i) #setting the duty cycle to 0

sleep(2)

for i in list(range(65, 89))[::-1]:
sleep(0.1) # give the ESC some time to warm up
motor.duty(i) #setting the duty cycle to 0

sleep(0.5) # give the ESC some time to warm up
motor.duty(90) #setting the duty cycle to 0
sleep(2)