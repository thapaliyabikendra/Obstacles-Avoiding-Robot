from picamera import PiCamera
from subprocess import Popen, PIPE
import threading
from time import sleep
import os, fcntl
import cv2
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
import RPi.GPIO as gpio
import time
import numpy as np
import random

moves = 3
learningRate = 0.9
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
epochs = 10
memory = []
max_memory = 500
iframe = 0
camera = PiCamera()
camera.resolution = (608, 608)
camera.capture('frame.jpg')
sleep(0.1)

yolo_proc = Popen(["./darknet",
                   "detect",
                   "./cfg/yolov3-tiny.cfg",
                   "./yolov3-tiny.weights",
                   "-thresh","0.1"],
                   stdin = PIPE, stdout = PIPE)

fcntl.fcntl(yolo_proc.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(608, 608, 3), activation = 'relu'))
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(Conv2D(128, (3, 3), activation = 'relu'))
model.add(Flatten())
model.add(Dense(512, activation = 'relu'))
model.add(Dense(3, activation = 'softmax'))
model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['acc'])

def init():
	gpio.setmode(gpio.BCM)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	gpio.setup(23, gpio.OUT)
	gpio.setup(24, gpio.OUT)

def forward(tf):
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(tf)
	gpio.cleanup()

def reverse(tf):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(tf)
	gpio.cleanup()
def left(tf):
	init()
	gpio.output(17, False)
	gpio.output(22, True)
	gpio.output(23, True)
	gpio.output(24, False)
	time.sleep(tf)
	gpio.cleanup()
def right(tf):
	init()
	gpio.output(17, True)
	gpio.output(22, False)
	gpio.output(23, False)
	gpio.output(24, True)
	time.sleep(tf)
	gpio.cleanup()

def getFrames():
	errors = True
	im = []
	try:
		stdout = yolo_proc.stdout.read()
		if 'Enter Image Path' in stdout:
			try:
				im = cv2.imread('predictions.png')
				cv2.imshow('yolov3-tiny', im)
				key = cv2.waitKey(1)
				print(im.shape)
			except Exception:
				pass
			camera.capture('frame.jpg')
			yolo_proc.stdin.write('frame.jpg\n')
		if len(stdout.strip())>0:
			print('get %s' % stdout)
			errors = False
	except Exception:
		pass
	return im, errors

for i in range(epochs):
	time.sleep(5)
	game_over = False
	input_img, errors = getFrames()
	errors = False
	reward = 0
	while game_over==False:
		if np.random.rand() <= epsilon:
			action = np.random.randint(0, moves, size=1)[0]
		else:
			output = model.predict(input_img)
			action = np.argmax(output[0])
		if int(action) == 0:
			forward(4)
		elif int(action) == 1:
			right(4)
		else:
			left(4)
		input_next_img, errors = getFrames()
		if errors == False:
			reward = reward + 1
		else:
			game_over = True
		if len(memory) >= max_memory:
			del memory[0]
		memory.append((input_img, action, reward, input_next_img, game_over))
		input_img = input_next_img
		if game_over:
			print("Game: {}/{}, Total Reward: {}".format(i, epochs, reward))
	if len(memory) > 32:
		batch_size = 32
	else:
		batch_size = len(memory)
	batch = random.sample(memory, batch_size)
	for input_img, action, reward, input_next_img, game_over in batch:
		target_reward = reward
		if game_over == False:
			target_reward = reward + learningRate * \
			np.amax(model.predict(input_next_img)[0])
		desired_target = model.predict(input_img)
		desired_target[0][action] = target_reward
		model.fit(input_img, desired_target, epochs=1, verbose=0)
	if epsilon > epsilon_min:
		epsilon *= epsilon_decay
