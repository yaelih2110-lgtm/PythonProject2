import pygame
def background_1():
    background_colour = (0,100,0)
    screen = pygame.display.set_mode((1220, 610))
    pygame.display.set_caption("The Flag")
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


background_1()
