import numpy as np
import random
import time
from motor import forward, left, right
from config import MAX_MEMORY, EPOCHS, MP_MN, FB_TIME, LR_TIME, WIDTH, HEIGHT
from cnn import checkModel
import camera

memory = []
moves = 3
learningRate = 0.9
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
model = checkModel()

for i in range(EPOCHS):
	game_over = False
	input_img, errors = camera.getImage()
	errors = False
	reward = 0
	while game_over==False:
		if np.random.rand() <= epsilon:
			action = np.random.randint(0, moves, size=1)[0]
		else:
			output = model.predict(input_img)
			print(output)
			action = np.argmax(output[0])
			print(action)
		if int(action) == 0:
			forward(FB_TIME)
			print('forward')
		elif int(action) == 1:
			right(LR_TIME)
			print('right')
		elif int(action) == 2:
			left(LR_TIME)
			print('left')
		input_next_img, errors = camera.getImage()
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
	dataset = np.ndarray(shape=(batch_size, WIDTH, HEIGHT, 1),  dtype=np.float32)
	label = np.ndarray(shape=(batch_size, 3 ),  dtype=np.float32)
	print(batch_size)
	i = 0
	for input_img, action, reward, input_next_img, game_over in batch:
		target_reward = reward
		if game_over == False:
			target_reward = reward + learningRate * \
			np.amax(model.predict(input_next_img)[0])
		"""
		desired_target = model.predict(input_img)
		desired_target[0][action] = target_reward
		"""
		desired_target = np.array([1, 0, 0])
		if action == 0:
			desired_target = np.array([1, 0, 0])
		elif action == 1:
			desired_target = np.array([0, 1, 0])
		elif action == 2:
			desired_target = np.array([0, 0, 1])			
		print(desired_target)
		dataset[i] = input_img
		label[i] = desired_target
		i = i + 1
	model.fit(x = dataset, y = label, epochs = 1, batch_size = 4, verbose = 1)
			
	if epsilon > epsilon_min:
		epsilon *= epsilon_decay

model.save(MP_MN)
