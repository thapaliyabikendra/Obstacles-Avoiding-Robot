import RPi.GPIO as gpio
from time import sleep
from config import SERVO
SERVO = 16
gpio.setmode(gpio.BCM)
gpio.setup(SERVO, gpio.OUT)

p = gpio.PWM(SERVO, 50)
p.start(7.5)
sleep(2)


def right():
	p.ChangeDutyCycle(2.5)
	sleep(2)

def front():
	p.ChangeDutyCycle(7.5)
	sleep(2)

def left():
	p.ChangeDutyCycle(12.5)
	sleep(2)


p.stop()
gpio.cleanup()


