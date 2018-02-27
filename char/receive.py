from RF24 import *
import time
from l293dClass import L293dPWM
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
pwm = GPIO.PWM(17, 100)
pwm.start(5)

leftMotor = L293dPWM(13, 19, 26)
leftMotor.init()

rightMotor = L293dPWM(16, 20, 21)
rightMotor.init()



pipes = [0xCDCDCDCDCD, 0xC1C2C3C4C5]

radio = RF24(25, 0)
radio.begin()

radio.setRetries(15,15)

radio.setChannel(0x60)
radio.setDataRate(RF24_250KBPS)
radio.setAutoAck(1)

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])

radio.startListening()

radio.printDetails()

dataReceiveSplit = {}
try:
    while True:
        if radio.available():
            dataReceiveSplit = radio.read(12)
            print "------"
            print radio.getDynamicPayloadSize()
            print "-------"
            print dataReceiveSplit
            print "!!!---------!!!"
            dataReceiveSplit = dataReceiveSplit.split('_')

            if (int(dataReceiveSplit[2]) == 1):
                rightMotor.forward()
            else:
                rightMotor.backward()

            if(int(dataReceiveSplit[0]) == 1):
                leftMotor.forward()
            else:
                leftMotor.backward()

            leftMotor.move(int(dataReceiveSplit[1]))
            rightMotor.move(int(dataReceiveSplit[3]))

            try:
                deg = int(dataReceiveSplit[4])
                duty = float(deg) / 10.0 + 2.5
                pwm.ChangeDutyCycle(duty)
            except:
                print "ex"

            time.sleep(0.1)
        else:
            leftMotor.move(0)
            rightMotor.move(0)
except KeyboardInterrupt:
    leftMotor.stop()
    rightMotor.stop()
    leftMotor.uninit()
    rightMotor.uninit()
    GPIO.cleanup()

