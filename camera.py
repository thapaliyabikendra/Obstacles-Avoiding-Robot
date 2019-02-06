from picamera import PiCamera
from subprocess import Popen, PIPE
import threading
from time import sleep
import os, fcntl
import cv2
import numpy as np
from configuration import WIDTH, HEIGHT, CHANNEL
iframe = 0
camera = PiCamera()
camera.resolution = (WIDTH, HEIGHT)
camera.capture('frame.jpg')

yolo_proc = Popen(["./darknet",
                   "detect",
                   "./cfg/yolov3-tiny.cfg",
                   "./yolov3-tiny.weights",
                   "-thresh","0.1"],
                   stdin = PIPE, stdout = PIPE)
fcntl.fcntl(yolo_proc.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

def getImage():
	errors = False
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
			errors = True
	except Exception:
		pass
	im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	im = im.reshape([-1, WIDTH, HEIGHT , CHANNEL])
	return im, errors
