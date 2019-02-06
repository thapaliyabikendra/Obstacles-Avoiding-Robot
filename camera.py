from picamera import PiCamera
from time import sleep
import cv2
import numpy as np
from configuration import WIDTH, HEIGHT, CHANNEL, MINIMUM_DISTANCE
from ultrasonic import getDistance

camera = PiCamera()
camera.resolution = (WIDTH, HEIGHT)

def getImage():
	errors = False
	output = np.empty((WIDTH, HEIGHT, CHANNEL), dtype=np.uint8)
	camera.start_preview()
	camera.capture(output,'bgr')
	im = cv2.imread(output)
	cv2.imshow('yolov3-tiny', im)
	key = cv2.waitKey(5)	
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im = im.reshape([-1, WIDTH, HEIGHT , CHANNEL])
	dist = getDistance()
	if(dist < MINIMUM_DISTANCE):
		errors = True
	return im, errors

getImage()
