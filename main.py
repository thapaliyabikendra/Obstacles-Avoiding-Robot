from picamera import PiCamera
from subprocess import Popen, PIPE
import os, fcntl
import cv2
import numpy as np
import re
import RPi.GPIO as gpio
import time
from config import FREQUENCY, DUTY_CYCLE, ENA, ENB, IN1, IN2, IN3, IN4, SERVO, WIDTH, HEIGHT, CHANNEL, MINIMUM_DISTANCE
from time import sleep

camera = PiCamera()
camera.resolution = (WIDTH, HEIGHT)
camera.rotation = 270
camera.capture('frame.jpg')

yolo_proc = Popen(["./darknet",
                   "detect",
                   "./cfg/yolov3-tiny.cfg",
                   "./yolov3-tiny.weights",
                   "-thresh","0.1"],
                   stdin = PIPE, stdout = PIPE)
fcntl.fcntl(yolo_proc.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(IN1, gpio.OUT)
	gpio.setup(IN2, gpio.OUT)
	gpio.setup(IN3, gpio.OUT)
	gpio.setup(IN4, gpio.OUT)
	gpio.setup(ENB, gpio.OUT)
	gpio.setup(ENA, gpio.OUT)
	
def right(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)
	gpio.output(IN1, True)
	gpio.output(IN2, False)
	gpio.output(IN3, True)
	gpio.output(IN4, False)
	time.sleep(tf)
	gpio.cleanup()

def left(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)
	gpio.output(IN1, False)
	gpio.output(IN2, True)
	gpio.output(IN3, False)
	gpio.output(IN4, True)
	time.sleep(tf)
	gpio.cleanup()

def forward(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)	
	gpio.output(IN1, False)
	gpio.output(IN2, True)
	gpio.output(IN3, True)
	gpio.output(IN4, False)
	time.sleep(tf)
	gpio.cleanup()

def reverse(tf):
	init()
	p1=gpio.PWM(ENB, FREQUENCY)
	p2=gpio.PWM(ENA, FREQUENCY)
	p1.start(DUTY_CYCLE)
	p2.start(DUTY_CYCLE)
	gpio.output(IN1, True)
	gpio.output(IN2, False)
	gpio.output(IN3, False)
	gpio.output(IN4, True)
	time.sleep(tf)
	gpio.cleanup()


def init1():
	gpio.setmode(gpio.BCM)
	gpio.setup(SERVO, gpio.OUT)
	p = gpio.PWM(SERVO, 50)
	p.start(7.5)
	sleep(2)
	return p

class servo:
	def righ():
		p = init1()
		p.ChangeDutyCycle(2.5)
		sleep(3)
		gpio.cleanup()
		return getImage()
	def fron():
		init1()
		gpio.cleanup()
		return getImage()
	def lef():
		p = init1()
		p.ChangeDutyCycle(12.5)
		sleep(3)
		gpio.cleanup()
		return getImage()

def getImage():
	error = False
	im = np.zeros((WIDTH, HEIGHT, 3), np.uint8)
	try:
		stdout = yolo_proc.stdout.read().decode('utf-8')
		if 'Enter Image Path' in stdout:
			try:
				im = cv2.imread('predictions.png')
				cv2.imshow('yolov3-tiny', im)
				key = cv2.waitKey(5)
				print(im.shape)
			except Exception:
				pass
			camera.capture('frame.jpg')
			yolo_proc.stdin.write(b'frame.jpg\n')
			yolo_proc.stdin.flush()
		if len(stdout.strip())>0:
			print('get %s' % stdout)
			a = re.search('person', stdout)
			b = re.search('chair', stdout)
			if a.group() == 'person' or b.group() == 'chair':
				error = True
	except Exception:
		pass
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im = im.reshape([-1, WIDTH, HEIGHT , CHANNEL])
	return error


for i in range(20):
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
camera.close()					



