from datetime  import datetime

WIDTH = 320
HEIGHT = 240
CP_WIDTH = 608
CP_HEIGHT = 608
CHANNEL = 1
EPOCHS = 5
MAX_MEMORY = 512
MODEL_PATH = 'trained_models/'
MODEL_NAME = 'OBSTACLESAVOIDINGROBOT' + datetime.now().strftime('%Y%m%d%H%M')+'.h5'
MP_MN = MODEL_PATH + MODEL_NAME
MINIMUM_DISTANCE = 20
THRESHOLD = 0
TRAIN_TIME =  100
MAXIMUM_MODEL_NUMBER  = 7
TRAINING_PATH = 'training_data/'
FREQUENCY = 1000
DUTY_CYCLE = 100
ENA = 20
ENB = 21
IN1 = 17
IN2 = 22
IN3 = 23
IN4 = 24
FB_TIME = 1
LR_TIME = 1.5