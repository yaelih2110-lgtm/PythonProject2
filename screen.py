import random
import pygame
import consts
from consts import GRASS, SOLDIER_INITIAL_PLACE

def background_1():
   background_colour = (0,100,0)
   screen = pygame.display.set_mode((consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT))
   pygame.display.set_caption("The Flag")
   screen.fill(background_colour)
   screen.blit(consts.FLAG, (1150,550))
   x_list=[]
   y_list=[]
   for i in range (20):
       while True:
           x=random.choice(range(consts.WINDOW_WIDTH-50))
           y=random.choice(range(consts.WINDOW_HEIGHT-50))
           if x not in x_list and y not in y_list:
               x_list.append(x)
               y_list.append(y)
               break
       screen.blit(GRASS, (x,y))
   pygame.display.flip()
   running = True
   while running:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
background_1()


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
if KEY_PRESSED[pygame.K_RETURN]:
    #print(56)
    background_night()
