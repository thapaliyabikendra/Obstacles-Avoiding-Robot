import pygame
import pygame.font
import picamera
import numpy as np
import time
from motor import forward, reverse
from motor import left as lef
from motor import right as righ
from config import HEIGHT, WIDTH, CP_WIDTH, CP_HEIGHT, TRAINING_PATH, FB_TIME, LR_TIME
from ultrasonic import getDistance

UP = LEFT = DOWN = RIGHT = False

def save_image_with_direction( direction):
	return TRAINING_PATH + direction + str(time.time()) + '.jpg'

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
        camera.resolution = ( WIDTH, HEIGHT)
        camera.rotation = 270
        camera.start_preview(fullscreen = False, window = (500, 50, CP_WIDTH, CP_HEIGHT))
        command = 'idle'
        while(True):
            up_key, down, left, right, change, stop = getKeys()
            getDistance()
            if stop:
                break
            if change:
                command = 'idle'
                if up_key:
                    command = 'forward'
                    forward(FB_TIME)
                elif down:
                    command = 'reverse'
                    reverse(FB_TIME)
                elif left:
                    command = 'left'
                    lef(LR_TIME)
                elif right:
                    command = 'right'
                    righ(LR_TIME)
            print(command)
            if(command in ('forward', 'right', 'left')):
                input_img = save_image_with_direction(command)
                camera.capture(input_img, use_video_port = True)
            clock.tick(10)
        pygame.quit()

def setupInteractiveControl():
    pygame.init()
    display_size = (500, 500)
    screen = pygame.display.set_mode(display_size)
    background = pygame.Surface(screen.get_size())
    color_white = (255, 255, 255)
    display_font = pygame.font.Font(None, 30)
    pygame.display.set_caption('RC Car Interactive Control')
    text = display_font.render('Use arrows to move', 1, color_white)
    text_position = text.get_rect(centerx=display_size[0] / 2)
    background.blit(text, text_position)
    screen.blit(background, (0, 0))
    pygame.display.flip()

def main():
	interactiveControl()

if __name__ == '__main__':
    main()
