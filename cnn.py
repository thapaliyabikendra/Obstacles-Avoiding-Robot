import os
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D,  Activation, GlobalAveragePooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from config import WIDTH, HEIGHT, CHANNEL, MODEL_PATH, MAXIMUM_MODEL_NUMBER, lr, beta_1, beta_2, decay
from date_from_filenames import getMinDate, getFileDetails, getMaxDate

#darknet tiny
def createModel():
    model = Sequential()

    model.add(Conv2D(16, (3, 3), input_shape=(WIDTH, HEIGHT, CHANNEL),padding = 'same', use_bias=False))    
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   
    model.add(MaxPooling2D(2, strides = 2, padding = 'same'))

    model.add(Conv2D(32, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   
    model.add(MaxPooling2D(2, strides = 2, padding = 'same'))

    model.add(Conv2D(16, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(128, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(16, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(128, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   
    model.add(MaxPooling2D(2, strides = 2, padding = 'same'))

    model.add(Conv2D(32, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(256, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(32, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(256, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   
    model.add(MaxPooling2D(2, strides = 2, padding = 'same'))

    model.add(Conv2D(64, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(512, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   
    
    model.add(Conv2D(64, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(512, (3, 3), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(128, (1, 1), padding = 'same', use_bias=False))
    model.add(BatchNormalization())
    model.add(LeakyReLU(alpha =0.1))   

    model.add(Conv2D(1000, (1, 1), padding = 'same', use_bias=False))   
    model.add(BatchNormalization())
    model.add(Activation('linear'))    
    model.add(GlobalAveragePooling2D())

    #model.add(Flatten())
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer = keras.optimizers.Adam(lr = lr, beta_1 = beta_1, beta_2 = beta_2, decay = decay), metrics = ['acc'])
    #model.summary()
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
