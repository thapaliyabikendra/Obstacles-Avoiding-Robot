import RPi.GPIO as gpio
from time import sleep
from config import SERVO
import camera
from motor import left, right, forward
import keras

gpio.setmode(gpio.BCM)
gpio.setup(SERVO, gpio.OUT)

p = gpio.PWM(SERVO, 50)
p.start(7.5)
sleep(2)

class servo:
	def righ():
		p.ChangeDutyCycle(2.5)
		sleep(3)
		return camera.getImage()
	def fron():
		p.ChangeDutyCycle(7.5)
		sleep(2)
		return camera.getImage()
	def lef():
		p.ChangeDutyCycle(12.5)
		sleep(3)
		return camera.getImage()

for i in range(20):
	servo.fron()


"""
for i in range(10):
	e = servo.fron()
	if e == False:
		forward(1)
		pass
	else:
		e = servo.righ()
		if e == False:
			right(1.25)
			e = servo.fron()
		else:
			e = servo.lef()
			if e == False:
				left(1.25)
				pass
				

"""

"""
for i in range(20):
	#servo.fron()
	#error = True
	error = camera.getImage()
	if error == False:		
		pass
	else:
		servo.lef()
		error = camera.getImage()
		if error == False:
			servo.fron()
			right(1.5)
		else:
			#lef()
			error = camera.getImage()
			if error == False:
				#fron()
				left(1.5)
"""			
p.stop()
gpio.cleanup()


