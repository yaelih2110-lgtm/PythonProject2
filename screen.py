from os import remove
from symbol import continue_stmt

import pygame
pygame.init()
KEY_PRESSED = pygame.key.get_pressed()

from PythonProject2.consts import WINDOW_HEIGHT


def background_green():
    background_colour = (0,100,0)
    screen = pygame.display.set_mode((1250, 625))
    pygame.display.set_caption("The Flag")
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if KEY_PRESSED[pygame.K_KP_ENTER]:
            running = False


green1 = (1, 59, 0)
def background_night():
    background_colour = (0, 0, 0)
    screen = pygame.display.set_mode((1250, 625))
    pygame.display.set_caption("The Flag (night mode)")
    screen.fill(background_colour)
    for i in range(0,1250,25):
        green_lines = pygame.Rect(i,0,1,625)
        pygame.draw.rect(screen,green1,green_lines)
    for j in range(0,625,25):
        green_lines = pygame.Rect(0, j, 1250, 1)
        pygame.draw.rect(screen, green1, green_lines)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


background_green()
background_night()
if KEY_PRESSED[pygame.K_KP_ENTER]: