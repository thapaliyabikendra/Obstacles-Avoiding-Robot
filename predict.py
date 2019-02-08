import numpy as np
from camera import getImage
from cnn import checkModel
from motor import forward, left, right

model = checkModel()
while True:
	input_img, errors = getImage()
	output = model.predict(input_img)
	print(output, output.shape )
	action = np.argmax(output[0])
	if int(action) == 0:
		forward(3)
		print('forward')
	elif int(action) == 1:
		right(3)
		print('right')
	else:
		left(3)
		print('left')

