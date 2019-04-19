from datetime  import datetime

#image
WIDTH = 320
HEIGHT = 240
CHANNEL = 1

#preview
CP_WIDTH = 608
CP_HEIGHT = 608

#training details
EPOCHS = 5
MAX_MEMORY = 256
MODEL_PATH = 'trained_models/'
TRAIN_TIME =  100

#model details
MAXIMUM_MODEL_NUMBER  = 7
TRAINING_PATH = 'training_data/'
MODEL_NAME = 'OBSTACLESAVOIDINGROBOT' + datetime.now().strftime('%Y%m%d%H%M')+'.h5'
MP_MN = MODEL_PATH + MODEL_NAME
epochs = 10
batch_size = 32

#motor driver L298N
FREQUENCY = 1000
DUTY_CYCLE = 90
ENA = 20
ENB = 21
IN1 = 17
IN2 = 22
IN3 = 23
IN4 = 24
FB_TIME = 0.8
LR_TIME = 0.8

#ultrasonic
TRIGGER = 14
ECHO = 15
THRESHOLD = 0
MINIMUM_DISTANCE = 20

#darknet model 
lr = 0.0005
beta_1 = 0.9
beta_2 = 0.999
decay = 0.0
