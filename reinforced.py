import numpy as np
import random
import time
from threading import Thread
from motor import forward, left, right
from camera import getImage
from configuration import MAX_MEMORY, EPOCHS, MP_MN
from cnn import checkModel

memory = []
moves = 3
learningRate = 0.9
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
model = checkModel()

for i in range(EPOCHS):
	game_over = False
	input_img, errors = getImage()
	errors = False
	reward = 0
	while game_over==False:
		if np.random.rand() <= epsilon:
			action = np.random.randint(0, moves, size=1)[0]
		else:
			output = model.predict(input_img)
			action = np.argmax(output[0])
		if int(action) == 0:
			forward(1)
			print('forward')
		elif int(action) == 1:
			right(1.25)
			print('right')
		else:
			left(1.25)
			print('left')
		input_next_img, errors = getImage()
		if errors == False:
			reward = reward + 1
		else:
			game_over = True
		if len(memory) >= MAX_MEMORY:
			del memory[0]
		memory.append((input_img, action, reward, input_next_img, game_over))
		input_img = input_next_img
		if game_over:
			print("Game: {}/{}, Total Reward: {}".format(i, EPOCHS, reward))
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
		t1 = Thread(target = model.fit, kwargs = dict(x= input_img, y = desired_target, epochs=1, verbose=0))
		t1.start()
	if epsilon > epsilon_min:
		epsilon *= epsilon_decay

model.save(MP_MN)
