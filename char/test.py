import time
from l293dClass import L293dPWM

leftMotor = L293dPWM(13, 19, 26) #in1, in2, en
#leftMotor = L293d(10, 11, 12) #in1, in2, en
leftMotor.init()


rightMotor = L293dPWM(16, 20, 21)
rightMotor.init()

try:
    #rightMotor.forward()


    rightMotor.move(100)
    leftMotor.move(100)
    while 1:
        '''rightMotor.forward()
        leftMotor.forward()
        time.sleep(2)
        rightMotor.stop()
        leftMotor.stop()
        time.sleep(2)
        rightMotor.move(50)
        leftMotor.move(50)
        rightMotor.backward()
        leftMotor.backward()
        time.sleep(2)
        rightMotor.stop()
        leftMotor.stop()
        time.sleep(2)
        rightMotor.move(10)
        leftMotor.move(100)'''
        rightMotor.forward()
        leftMotor.forward()
        for i in range(0, 100):
            rightMotor.move(i)
            leftMotor.move(i)
            time.sleep(0.1)
        rightMotor.backward()
        leftMotor.backward()
        for i in range(0, 100):
            rightMotor.move(i)
            leftMotor.move(i)
            time.sleep(0.1)
except KeyboardInterrupt:
    leftMotor.uninit()
    rightMotor.uninit()

'''import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

o1 = 2
o2 = 3
e =  4

GPIO.setup(o1, GPIO.OUT)
GPIO.setup(o2, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)

try:
    while 1:
        GPIO.output(o1, GPIO.LOW)
        GPIO.output(o2, GPIO.HIGH)
        GPIO.output(e, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
'''