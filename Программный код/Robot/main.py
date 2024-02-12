from flask import Flask, request, jsonify
from servo import set_angle, set_angle_two_servo, posUp, posMd, posBt, posZero
from motor import move3
import sys
import time
import RPi.GPIO as IO
import drivers
import picamera
from PIL import Image
from pyzbar import pyzbar

app = Flask(__name__)
isLaunch = False
isConnect = False
orders = []
cargos = ["Vinti","Gauki","Shuibi","Shpilki","Podshipniki","Lineini napravlashie","Vali","Dvigatel","Datchiki"]
cucle = 1
recognition_cargo = 'null'
position_cargo = 0

IO.setwarnings(False)
IO.setmode(IO.BOARD)
pinLedR = 16
IO.setup(pinLedR, IO.OUT)
pinLedG = 18
IO.setup(pinLedG, IO.OUT)
pinLedB = 22
IO.setup(pinLedB, IO.OUT)

servo_pin1 = 35
servo_pin2 = 33
servo_pin3 = 31
servo_pin4 = 36
servo_pin5 = 40

in1 = 11
in2 = 13
en_a = 7

display = drivers.Lcd()

test = []

hqCamera = picamera.PiCamera()

stream = io.BytesIO()

IO.setup(in1,IO.OUT)
IO.setup(in2,IO.OUT)
IO.setup(en_a,IO.OUT)
IO.output(in1,IO.LOW)
IO.output(in2,IO.LOW)

IO.output(pinLedR, 1)

@app.route('/launch')
def launch():
    global isLaunch, isConnect
    if (not isConnect):
        if (isLaunch):
            IO.output(pinLedR, 0)
            IO.output(pinLedG, 1)
            set_angle(0, servo_pin3)
            display.lcd_clear()
            rec()
            isLaunch = False
            catch()
            return "Запущен"
        else:
            isLaunch = True
            IO.output(pinLedR, 1)
            IO.output(pinLedG, 0)
            set_angle(0, servo_pin3)
            posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
            move3(0, in1, in2, en_a)
            display.lcd_clear()
            return "Выключен"

@app.route('/connect')
def connect():
    global isConnect, cucle
    if (isConnect):
        isConnect = False
        IO.output(pinLedB, 1)
        if cucle < 3:
            cucle += 1
        else:
            cucle = 1
        print(cucle)
        return "Подключено"
    else:
        isConnect = True
        IO.output(pinLedB, 0)
        return "Отключен"

@app.route('/order', methods=['GET'])
def order():
    global orders, isConnect, isLaunch, test
    orders = []

    for i in range(1, 10):
        key = str(i)
        value = request.args.get(key, default='False')
        orders.append(value)

    if(not isConnect and not isLaunch):
        catch()
        return str(orders)
    else:
        return "Ok"

@app.route('/recognition')
def recognition():
    global recognition_cargo
    return recognition_cargo

@app.route('/info')
def info():
    global isConnect, isLaunch
    return str(isConnect*1) + str(isLaunch*1)

def recServo():
    global position_cargo, display, cargos, recognition_cargo
    #posUp(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
    #time.sleep(3)#1
<<<<<<< HEAD
    set_angle_two_servo(-30, servo_pin2, servo_pin1)
    set_angle_two_servo(65, servo_pin5, servo_pin4)
=======
    set_angle_two_servo(-70, servo_pin2, servo_pin1)
    set_angle_two_servo(55, servo_pin5, servo_pin4)
>>>>>>> 898a6b57e13d51fac0c02abd09563e14a9898f6f
    time.sleep(3)
    display.lcd_clear()
    capture_image() 
    display.lcd_display_string(str(process_image()), 2)
    recognition_cargo = process_image()

    #posMd(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
    #time.sleep(3)#2
    set_angle_two_servo(-70, servo_pin2, servo_pin1)
    set_angle_two_servo(35, servo_pin5, servo_pin4)
    time.sleep(3)    
    display.lcd_clear()
    capture_image() 
    display.lcd_display_string(str(process_image()), 2)
    recognition_cargo = process_image()

    #posBt(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
    #time.sleep(3)#3
    set_angle_two_servo(-70, servo_pin2, servo_pin1)
    set_angle_two_servo(20, servo_pin5, servo_pin4)
    time.sleep(3)
    display.lcd_clear()
    capture_image() 
    display.lcd_display_string(str(process_image()), 2)
    recognition_cargo = process_image()

    display.lcd_clear()


def rec():
    global position_cargo
    position_cargo = 0
    posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
    move3(0, in1, in2, en_a)
    time.sleep(1)
    move3(1, in1, in2, en_a)
    recServo()
    time.sleep(1)
    move3(2, in1, in2, en_a)
    recServo()
    time.sleep(1)
    move3(3, in1, in2, en_a)
    recServo()
    time.sleep(1)
    posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
    move3(0, in1, in2, en_a)

def capture_image():
    hqCamera.start_preview()
    time.sleep(2)
    hqCamera.capture(stream, format='jpeg')
    hqCamera.stop_preview()
    stream.seek(0)
def process_image():
    image = Image.open(stream)
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        qrcode_data = barcode.data.decode("utf-8")
        qrcode_type = barcode.type
        print(f"Распознанный QR-код: {qrcode_data}, Тип: {qrcode_type}")

def catch():
    global orders, test
    if orders:
        move3(0, in1, in2, en_a)
        posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
        for i in range(len(orders)):
            if orders[i] == "True":
                if i in [0, 1, 2]:
                    move3(1, in1, in2, en_a)
<<<<<<< HEAD
                    set_angle(23, servo_pin3)
=======
                    set_angle(20, servo_pin3)
>>>>>>> 898a6b57e13d51fac0c02abd09563e14a9898f6f
                    time.sleep(1)
                    if i in [0]:
                        posUp(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                    elif i in [1]:
                        posMd(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                    elif i in [2]:
                        posBt(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                elif i in [3, 4, 5]:
                    move3(2, in1, in2, en_a)
<<<<<<< HEAD
                    set_angle(23, servo_pin3)
=======
                    set_angle(20, servo_pin3)
>>>>>>> 898a6b57e13d51fac0c02abd09563e14a9898f6f
                    if i in [3]:
                        posUp(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                    elif i in [4]:
                        posMd(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                    elif i in [5]:
                        posBt(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                elif i in [6, 7, 8]:
                    move3(3, in1, in2, en_a)
<<<<<<< HEAD
                    set_angle(23, servo_pin3)
=======
                    set_angle(20, servo_pin3)
>>>>>>> 898a6b57e13d51fac0c02abd09563e14a9898f6f
                    if i in [6]:
                        posUp(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                    elif i in [7]:
                        posMd(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                    elif i in [8]:
<<<<<<< HEAD
                        posBt(servo_pin2, servo_pin1, servo_pin5, servo_pin4, servo_pin3)
                set_angle(0, servo_pin3)
                move3(0, in1, in2, en_a)
                time.sleep(1)
=======
                        posBt(servo_pin2, servo_pin1, servo_pin5, servo_pin4)

                time.sleep(1)
                set_angle(0, servo_pin3)
                time.sleep(2)
                posZero(servo_pin2, servo_pin1, servo_pin5, servo_pin4)
                time.sleep(3)
                move3(0, in1, in2, en_a)
                time.sleep(1)
                set_angle(20, servo_pin3)
                time.sleep(2)
                set_angle(0, servo_pin3)
>>>>>>> 898a6b57e13d51fac0c02abd09563e14a9898f6f

if __name__ == '__main__':
    try:
        app.run(debug=True, host="0.0.0.0", port="3000")
    except KeyboardInterrupt:
        GPIO.cleanup()
