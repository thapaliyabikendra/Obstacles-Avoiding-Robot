import os
import re
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from cnn import checkModel
from config import MP_MN, TRAINING_PATH, WIDTH, HEIGHT, CHANNEL, epochs, batch_size


labels = re.compile(r'^[a-z]*')
model = checkModel()

def getDesiredTarget(f):
	matched = labels.search(f)
	return matched

def getTarget(desired_target):
	if desired_target.group(0) == 'forward':
		target = np.array([1, 0, 0])
	elif desired_target.group(0) == 'right':
		target = np.array([0, 1, 0])
	elif desired_target.group(0) == 'left':
		target = np.array([0, 0, 1])
	return target


def getDataset():
	filenames = os.listdir(TRAINING_PATH)
	dataset = np.ndarray(shape=(len(filenames), WIDTH, HEIGHT),  dtype=np.float32)
	label = np.ndarray(shape=(len(filenames), 3 ),  dtype=np.float32)
	for i, f in enumerate(filenames):
		desired_target = getDesiredTarget(f)
		desired_target = getTarget(desired_target)
		input_img  = cv2.imread(TRAINING_PATH + f, 0)
		dataset[i] = input_img
		label[i] = desired_target
	return dataset, label

def train():
	X, Y = getDataset()
	X = X.reshape([-1, WIDTH, HEIGHT, CHANNEL])
	X = X / 255.
	train_X, valid_X, train_label, valid_label = train_test_split(X, Y, test_size=0.2, random_state=13)
	model.fit(train_X, train_label, epochs = epochs, verbose = 1, batch_size = batch_size, validation_data=(valid_X, valid_label))


def main():
	train()
	model.save(MP_MN)
	print('TRAINED MODEL')

if __name__ == '__main__':
	main()
