from picamera import PiCamera
from time import sleep
import cv2
import numpy as np
from configuration import WIDTH, HEIGHT, CHANNEL, MINIMUM_DISTANCE, CP_WIDTH, CP_HEIGHT
from ultrasonic import getDistance

camera = PiCamera()
camera.resolution = (HEIGHT, WIDTH)

def getImage():
	errors = False
	im = np.empty(( WIDTH, HEIGHT, 3), dtype=np.uint8)
	camera.start_preview(fullscreen = False, window = (0, 0, CP_WIDTH, CP_HEIGHT))
	camera.capture(im, 'bgr', use_video_port = True)
	#cv2.imshow('yolov3-tiny', im)
	#key = cv2.waitKey(5)
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im = im.reshape([-1, WIDTH, HEIGHT , CHANNEL])
	dist = getDistance()
	if(dist < MINIMUM_DISTANCE):
		errors = True
	return im, errors

if __name__ == '__main__':
	getImage()
