import time
import RPi.GPIO as GPIO

def set_angle(angle, servo_pin):
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, 50)
    pwm.start(8)
    duty = (angle+90)/18+2
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.1)
    pwm.stop()

def set_angle_two_servo(angle, servo_pin1, servo_pin2):
    GPIO.setup(servo_pin1, GPIO.OUT)
    GPIO.setup(servo_pin2, GPIO.OUT)
    pwm1 = GPIO.PWM(servo_pin1, 50)
    pwm2 = GPIO.PWM(servo_pin2, 50)
    pwm1.start(8)
    pwm2.start(8)
    duty1 = (angle+90)/18+2
    duty2 = (90-angle)/18+2
    pwm1.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(0.1)
    pwm1.stop()
    pwm2.stop()

def servo_start(servo_pin1, servo_pin2, servo_pin3, servo_pin4):
    pwm1 = GPIO.PWM(servo_pin1, 50)
    pwm2 = GPIO.PWM(servo_pin2, 50)
    pwm3 = GPIO.PWM(servo_pin3, 50)
    pwm4 = GPIO.PWM(servo_pin4, 50)
    pwm1.start(8)
    pwm2.start(8)
    pwm3.start(8)
    pwm4.start(8)
    
    duty1 = (30+90)/18+2
    duty2 = (90-30)/18+2
    duty3 = ((30)+90)/18+2
    duty4 = (90-(30))/18+2
    
    pwm1.ChangeDutyCycle(duty1)
    pwm2.ChangeDutyCycle(duty2)
    pwm3.ChangeDutyCycle(duty3)
    pwm4.ChangeDutyCycle(duty4)
    time.sleep(1)
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()
    
def posUp(servo_pin2, servo_pin1, servo_pin5, servo_pin4):
    n1=-90
    n2=65
    while n1!=45 and n2!=-20:
        set_angle_two_servo(n2, servo_pin5, servo_pin4)
        set_angle_two_servo(n1, servo_pin2, servo_pin1)
        
        n1+=27
        n2-=17

def posMd(servo_pin2, servo_pin1, servo_pin5, servo_pin4):
    n1=-90
    n2=65
    while n1!=45 and n2!=-45:
        set_angle_two_servo(n1, servo_pin2, servo_pin1)
        set_angle_two_servo(n2, servo_pin5, servo_pin4)
        n1+=27
        n2-=22

def posBt(servo_pin2, servo_pin1, servo_pin5, servo_pin4):
    n1=-90
    n2=65
    while n1!=45 and n2!=-45:
        set_angle_two_servo(n1, servo_pin2, servo_pin1)
        set_angle_two_servo(n2, servo_pin5, servo_pin4)
        n1+=27
        n2-=22

def posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4):
    set_angle_two_servo(-30, servo_pin2, servo_pin1)
    time.sleep(1)
    set_angle_two_servo(40, servo_pin5, servo_pin4)
