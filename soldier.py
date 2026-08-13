import random
import pygame
import consts


def create_screen():
    grid=[]
    for i in range(consts.height):
        grid.append([])
        for j in range(consts.width):
            grid[i].append(['EMPTY'])
    return grid


def grass(grid):
    for i in range(20):
        x=random.choice(0,consts.height)
        y=random.choice(0,consts.width)
        if grid[x][y]=='EMPTY':
            grid[x][y]=consts.GRASS
    return grid
def mines(grid,x,y):
    for i in range(20):
        x = random.choice(0, consts.height)
        y = random.choice(0, consts.width)
        if grid[x][y] == 'EMPTY':
            grid[x][y]=consts.MINE
    return grid

create_screen()