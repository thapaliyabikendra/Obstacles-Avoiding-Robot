from time import sleep,time
from picamera import PiCamera
import numpy as np
import matplotlib.pyplot as plt
import cv2

camera = PiCamera()
camera.resolution = (320, 240)
camera.rotation = 270
camera.framerate = 24
output = np.empty((240, 320, 3), dtype=np.uint8)
output2 = np.empty((240, 320, 3), dtype=np.uint8)
def get_image():	
	camera.capture(output, 'rgb')
	return output
def show_image():
	camera.capture(output2, 'bgr')
	GrayImg = cv2.cvtColor(output2, cv2.COLOR_BGR2GRAY)
	input_img = GrayImg.reshape(240 , 320, 1)
	plt.imshow(GrayImg, cmap = 'gray')
	plt.show()
camera.close()





