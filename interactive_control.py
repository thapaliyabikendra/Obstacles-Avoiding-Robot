import time
import pygame
import pygame.font
import picamera
from motor import forward, reverse
from motor import left as lef
from motor import right as righ
from configuration import WIDTH, HEIGHT
from ultrasonic import getDistance

UP = LEFT = DOWN = RIGHT = False

def get_keys():
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


def interactive_control():
    setup_interactive_control()
    clock = pygame.time.Clock()
    with picamera.PiCamera() as camera:
        camera.start_preview(fullscreen = False, window = (500, 50, WIDTH, HEIGHT))			
        command = 'idle'
        while True:
            up_key, down, left, right, change, stop = get_keys()
            getDistance()
            if stop:
                break
            if change:
                command = 'idle'
                if up_key:
                    command = 'forward'
                    forward(1)
                elif down:
                    command = 'reverse'
                    reverse(1)

                append = lambda x: command + '_' + x if command != 'idle' else x

                if left:
                    command = append('left')
                    lef(1.25)
                elif right:
                    command = append('right')
                    righ(1.25)
            print(command)
            clock.tick(30)
        pygame.quit()

def setup_interactive_control():
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
    interactive_control()

if __name__ == '__main__':
    main()
