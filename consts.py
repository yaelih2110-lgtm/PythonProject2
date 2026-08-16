import pygame

BACKGROUND_COLOR=(34,139,34)
WINDOW_HEIGHT = 625
WINDOW_WIDTH =1250
grass=pygame.image.load('grass.png')
GRASS=pygame.transform.scale(grass, (2*(WINDOW_WIDTH/50), 2*(WINDOW_HEIGHT/25)))
flag=pygame.image.load('flag.png')
FLAG=pygame.transform.scale(flag, (4*(WINDOW_WIDTH/50),3*WINDOW_HEIGHT/25))
MAIN='main.png'
soldier=pygame.image.load('soldier.png')
soldier_size=pygame.transform.scale(soldier,(2*(WINDOW_WIDTH/50),4*(WINDOW_HEIGHT/25)))
SOLDIER_INITIAL_PLACE=pygame.Rect((0,0),(2*(WINDOW_WIDTH/50),4*(WINDOW_HEIGHT/25)))
LOSE_MESSAGE = "You Lost!"
BLACK = (0, 0, 0)
LOSE_FONT_SIZE = int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = BLACK
LOSE_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))
WIN_MESSAGE = "You Won!"
WIN_FONT_SIZE = LOSE_FONT_SIZE
WIN_COLOR = (89, 89, 89)
WIN_LOCATION = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (WIN_FONT_SIZE / 2))
