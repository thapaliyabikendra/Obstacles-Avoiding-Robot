import time
import motor
from cnn import model
from picameral import input_img
moves = 3
learningRate = 0.9
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
epochs = 100
memory = []
max_memory = 500
for i in range(epochs):
	time.sleep(5)
	game_over = False
	input_img, errors = getFrames()
	errors = False
	reward = 0
	while game_over==False:
		if np.random.rand() <= epsilon:
			action = np.random.randint(0, moves, size=1)[0]
		else:
			output = model.predict(input_img)
			action = np.argmax(output[0])
		if int(action) == 0:
			motor.forward()
		elif int(action) == 1:
			motor.right()
		else:
			motor.left()
		input_next_img, errors = getFrames()
		if errors == False:
			reward = reward + 1
		else:
			game_over = True
		if len(memory) >= max_memory:
			del memory[0]
		memory.append((input_img, action, reward, input_next_img, game_over))
		input_img = input_next_img
		if game_over:
			print("Game: {}/{}, Total Reward: {}".format(i, epochs, reward))
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
		model.fit(input_img, desired_target, epochs=1, verbose=0)
	if epsilon > epsilon_min:
		epsilon *= epsilon_decay
