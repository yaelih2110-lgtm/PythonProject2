import random
import pygame
import consts


def create_screen(width,height):
    grid=[]
    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(['EMPTY'])
    return grid


def grass(grid,x,y):
    for i in range(20):
        random.choice(x)
        random.choice(y)
        if grid[x][y]=='EMPTY':
            grid[x][y]=consts.GRASS
    return grid
def mines(grid,x,y):
    for i in range(20):
        random.choice(x)
        random.choice(y)
        if grid[x][y]=='EMPTY':
            grid[x][y]=consts.MINE
    return grid



