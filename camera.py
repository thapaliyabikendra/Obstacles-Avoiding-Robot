from picamera import PiCamera
import time
import cv2
import numpy as np
from configuration import WIDTH, HEIGHT, CHANNEL, MINIMUM_DISTANCE, CP_WIDTH, CP_HEIGHT, TRAINING_PATH
from ultrasonic import getDistance

def getImage():
	camera = PiCamera()
	camera.resolution = (HEIGHT, WIDTH)
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

def save_image_with_direction( direction):
	return TRAINING_PATH + direction + str(time.time()) + '.jpg'

if __name__ == '__main__':
	getImage()
