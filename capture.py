from picamera import PiCamera
import time
import cv2
import numpy as np
from config import WIDTH, HEIGHT, CHANNEL, MINIMUM_DISTANCE, CP_WIDTH, CP_HEIGHT
from ultrasonic import getDistance

camera = PiCamera()

def getImage():
	camera.resolution = (HEIGHT, WIDTH)
	camera.capture('/var/www/html/image.jpg')

if __name__ == '__main__':
	getImage()
