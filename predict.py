import numpy as np
from camera import getImage
from cnn import checkModel
from motor import forward, left, right
from config import FB_TIME, LR_TIME

model = checkModel()
while True:
	input_img, errors = getImage()
	output = model.predict(input_img)
	print(output, output.shape )
	action = np.argmax(output[0])
	if int(action) == 0:
		forward(FB_TIME)
		print('forward')
	elif int(action) == 1:
		right(LR_TIME)
		print('right')
	elif int(action) == 2:
		left(LR_TIME)
		print('left')

