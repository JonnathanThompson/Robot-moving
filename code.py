import time #imports time libary that are needed to run this code
import board #imports board libary that are needed to run this code
import digitalio #imports digitalio libary that are needed to run this code
import pwmio #imports libaries that are needed to run this code

from adafruit_motor import motor #imports a small section of adafruit_motor libary

left_motor_forward = board.GP12 #Initilizes the varibale left_motor_forward and attaches it to GP12
left_motor_backwards = board.GP13 #Initilizes the varibale left_motor_backwards and attaches it to GP13

pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(left_motor_backwards, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Intilaizes Left_Motor and configuration line and it is required
Left_Motor_speed = 0 #Intilaizes the variable Left_Motor_speed to 0


right_motor_forward = board.GP14 #Initilizes the varibale right_motor_forward and attaches it to GP14
right_motor_backwards = board.GP15 #Initilizes the varibale right_motor_backwards and attaches it to GP15


pwm_La = pwmio.PWMOut(right_motor_forward, frequency=10000) #Tells the pico that this component is an output (and some other configuration)
pwm_Lb = pwmio.PWMOut(right_motor_backwards, frequency=10000) #Tells the pico that this component is an output (and some other configuration)

Right_Motor = motor.DCMotor(pwm_La, pwm_Lb) #Intilaizes Right_Motor and configuration line and it is required
Right_Motor_speed = 0 #Intilaizes the variable Right_Motor_speed to 0




while True:

   Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(3.1)
   
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.5)
   
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(1.7)
   
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.5)
   
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.8)
   
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.4)
   
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.7)
   
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.6)
   
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.5)
   
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(.2)
   
    Left_Motor_speed = 1 #Left motor forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Right motor forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(2.7)
   
