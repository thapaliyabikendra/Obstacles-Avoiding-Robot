import cv2
import numpy as np
from cnn import checkModel
from configuration import MP_MN, TRAINING_PATH, WIDTH, HEIGHT , CHANNEL
import os
import re

labels = re.compile(r'^[a-z]*')
model = checkModel()

def getDesiredTarget(f):
	matched = labels.search(f)
	return matched

def getTarget(desired_target):
	if desired_target == 'forward':
		target = np.array([[1, 0, 0]])
	elif desired_target == 'right':
		target = np.array([[0, 1, 0]])
	else:
		target = np.array([[0, 0, 1]])
	return target

	
def train():
	filenames = os.listdir(TRAINING_PATH)
	for f in filenames:
		desired_target = getDesiredTarget(f)
		desired_target = getTarget(desired_target)
		input_img = cv2.imread('training_data/' + f)
		input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
		input_img = input_img.reshape([-1, WIDTH, HEIGHT , CHANNEL])
		model.fit(input_img, desired_target, epochs=1, verbose=1)
	
def main():
	train()
	model.save(MP_MN)
	print('TRAINED MODEL')

if __name__ == '__main__':
	main()
