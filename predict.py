from camera import getImage


while True:
	input_next_img, errors = getImage()
	if int(action) == 0:
		forward(3)
		print('forward')
	elif int(action) == 1:
		right(3)
		print('right')
	else:
		left(3)
		print('left')

