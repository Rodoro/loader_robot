import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

position = 0

def move3(target, in1, in2, en_a):
   global position
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(38, GPIO.IN)

   q=GPIO.PWM(en_a,100)
   q.start(90)

   while target > position:
      print(position+1)
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)
      time.sleep(0.4)
      while GPIO.input(38) == False:
         time.sleep(0.1)
      position += 1
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)
      if target == position:
         time.sleep(5)
   
   while target < position:
      print(position-1)
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)
      time.sleep(0.4)
      while GPIO.input(38) == False:
         time.sleep(0.1)
      position -= 1
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)
      if target == position:
         time.sleep(5)
