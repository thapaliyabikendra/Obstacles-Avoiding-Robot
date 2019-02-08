import os
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from configuration import WIDTH, HEIGHT, CHANNEL, MODEL_PATH, MAXIMUM_MODEL_NUMBER
from date_from_filenames import getMinDate, getFileDetails, getMaxDate

def createModel():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), input_shape=(WIDTH, HEIGHT, CHANNEL), activation='relu'))
	model.add(MaxPooling2D(2))
	model.add(Conv2D(32, (3, 3), activation='relu'))
	model.add(MaxPooling2D(2))
	model.add(Flatten())
	model.add(Dense(32, activation='relu'))
	model.add(Dense(3, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics = ['acc'])
	return model

def loadModel():
   model = load_model(getMaxDate())
   print("MODEL LOADED !!!")
   return model

def checkModel():
	delete_old_models()
	_, n = getFileDetails()
	if n == 0:
		model = createModel()
	else:
		model = loadModel()
	return model

def delete_old_models():
	_, no_of_model  = getFileDetails()
	while (no_of_model > MAXIMUM_MODEL_NUMBER):
		filename = getMinDate()
		os.remove(filename)
		print("MODEL DELETED !!! \n", filename)
		_, no_of_model  = getFileDetails()	

if __name__ == '__main__':
	createModel()
	loadModel()
