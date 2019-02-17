from camera import getImage
from cnn import load_trained_model

model = load_trained_model()
while True:
	input_next_img, errors = getImage()
	output = model.predict(input_img)
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

