import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class L293d:
	input1 = 0
	input2 = 0
	enable = 0
	
	def __init__(self, input1, input2, enable):
		self.input1 = input1
		self.input2 = input2
		self.enable = enable
	
	def init(self):
		GPIO.setup(self.input1, GPIO.OUT)
		GPIO.setup(self.input2, GPIO.OUT)
		GPIO.setup(self.enable, GPIO.OUT)
	
	
	def forward(self):
		GPIO.output(self.input1, GPIO.HIGH)
		GPIO.output(self.input2, GPIO.LOW)

	def backward(self):
		GPIO.output(self.input1, GPIO.LOW)
                GPIO.output(self.input2, GPIO.HIGH)

	def move(self):
		GPIO.output(self.enable, GPIO.HIGH)

	def stop(self):
		GPIO.output(self.input2, GPIO.LOW)


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class L293dPWM:
	input1 = 0
	input2 = 0
	enable = 0

	def __init__(self, input1, input2, enable):
		self.input1 = input1
		self.input2 = input2
		self.enable = enable

	def init(self):
		GPIO.setup(self.input1, GPIO.OUT)
		GPIO.setup(self.input2, GPIO.OUT)
		GPIO.setup(self.enable, GPIO.OUT)
		self.enable = GPIO.PWM(self.enable, 100)
		self.enable.start(0)

	def forward(self):
		GPIO.output(self.input1, GPIO.HIGH)
		GPIO.output(self.input2, GPIO.LOW)

	def backward(self):
		GPIO.output(self.input1, GPIO.LOW)
		GPIO.output(self.input2, GPIO.HIGH)

	def move(self, percent):
		self.enable.ChangeDutyCycle(percent)

	def stop(self):
		self.enable.ChangeDutyCycle(0)

