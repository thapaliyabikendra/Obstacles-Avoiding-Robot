from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from configuration import WIDTH, HEIGHT, CHANNEL, MODEL_PATH
from get_maxdate_from_filenames import get_maxdate
def create_model():
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

def load_trained_model():
   print(get_maxdate())
   model = load_model(get_maxdate())
   return model
