import random
import pygame
def background_color1():
    background_color = ((0, 100, 0))
    screen = pygame.display.set_mode((1420,820))
    pygame.display.set_caption("The Flag")
    screen.fill(background_color)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False