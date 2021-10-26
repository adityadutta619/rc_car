# Change pins as needed

import machine
servo_pin = machine.Pin(13)
servo = machine.PWM(servo_pin, freq=50)

# Goes from 40 to 115
servo.duty(77)

motor_pin = machine.Pin(14)
motor = machine.PWM(motor_pin, freq=50)

while True:
    # Arm the ESC******************
    
    sleep(2) # give the ESC some time to warm up
    motor.duty(90) #setting the duty cycle to 0
    sleep(2)
    
    