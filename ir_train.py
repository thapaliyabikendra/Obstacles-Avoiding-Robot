import time
import numpy as np
import pygame
import pygame.font
import picamera
import cv2
from  threading import Thread
from cnn import checkModel
from motor import forward, reverse
from motor import left as lef
from motor import right as righ
from configuration import WIDTH, HEIGHT, CHANNEL, CP_WIDTH, CP_HEIGHT, MP_MN, TRAIN_TIME
from ultrasonic import getDistance

UP = LEFT = DOWN = RIGHT = False
model = checkModel()
def getKeys():
    change = False
    stop = False
    key_to_global_name = {
        pygame.K_LEFT: 'LEFT',
        pygame.K_RIGHT: 'RIGHT',
        pygame.K_UP: 'UP',
        pygame.K_DOWN: 'DOWN',
        pygame.K_ESCAPE: 'QUIT',
        pygame.K_q: 'QUIT',
    }
    for event in pygame.event.get():
        if event.type in {pygame.K_q, pygame.K_ESCAPE}:
            stop = True
        elif event.type in {pygame.KEYDOWN, pygame.KEYUP}:
            down = (event.type == pygame.KEYDOWN)
            change = (event.key in key_to_global_name)
            if event.key in key_to_global_name:
                globals()[key_to_global_name[event.key]] = down
    return (UP, DOWN, LEFT, RIGHT, change, stop)


def interactiveControl():
    setupInteractiveControl()
    clock = pygame.time.Clock()
    with picamera.PiCamera() as camera:
        camera.resolution = (HEIGHT, WIDTH)
        camera.start_preview(fullscreen = False, window = (500, 50, CP_WIDTH, CP_HEIGHT))
        command = 'idle'
        start_time = time.time()
        now = 0
        while(now <= TRAIN_TIME):
            now = time.time() - start_time
            desired_target = np.array([[1, 0, 0]])
            input_img = np.empty(( WIDTH, HEIGHT, 3), dtype=np.uint8)
            camera.capture(input_img, 'bgr', use_video_port = True)
            input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            input_img = input_img.reshape([-1, WIDTH, HEIGHT , CHANNEL]) 
            up_key, down, left, right, change, stop = getKeys()
            getDistance()
            if stop:
                break
            if change:
                command = 'idle'
                if up_key:
                    command = 'forward'
                    desired_target = np.array([[1, 0, 0]])
                    t1 = Thread(target = forward, args = (1,))
                    t1.start()
                elif down:
                    command = 'reverse'
                    reverse(1)
                append = lambda x: command + '_' + x if command != 'idle' else x
                if left:
                    command = append('left')
                    desired_target = np.array([[0, 0, 1]])
                    t2 = Thread(target = lef, args = (1.25,))
                    t2.start()
                elif right:
                    command = append('right')
                    desired_target = np.array([[0, 1, 0]])
                    t3 = Thread(target = righ, args = (1.25,))
                    t3.start()
            print(command)
            print('Time left : ', (TRAIN_TIME - now), ' s')
            if command in ('forward', 'left', 'right'):
                model.fit(input_img, desired_target, epochs=1, verbose=0)
            clock.tick(0)
        pygame.quit()

def setupInteractiveControl():
    pygame.init()
    display_size = (400, 400)
    screen = pygame.display.set_mode(display_size)
    background = pygame.Surface(screen.get_size())
    color_white = (255, 255, 255)
    display_font = pygame.font.Font(None, 40)
    pygame.display.set_caption('RC Car Interactive Control')
    text = display_font.render('Use arrows to move', 1, color_white)
    text_position = text.get_rect(centerx=display_size[0] / 2)
    background.blit(text, text_position)
    screen.blit(background, (0, 0))
    pygame.display.flip()

def main():
	print('Training Time: ', (TRAIN_TIME/60), " min")
	interactiveControl()
	print('TIME UP !!!')
	model.save(MP_MN)

if __name__ == '__main__':
    main()
