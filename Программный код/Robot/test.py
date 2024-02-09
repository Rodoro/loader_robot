from servo import set_angle, set_angle_two_servo, posUp, posMd, posBt, posZero
import RPi.GPIO as IO
servo_pin1 = 35
servo_pin2 = 33
servo_pin3 = 31
servo_pin4 = 36
servo_pin5 = 40
IO.setwarnings(False)
IO.setmode(IO.BOARD)
posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
