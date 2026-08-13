import random
import pygame
import consts
grid=[]

def create_screen():
    for i in range(consts.height):
        grid.append([])
        for j in range(consts.width):
            grid[i].append(['EMPTY'])
    return grid


def grass(grid):
    for i in range(20):
        x=random.choice(consts.height)
        y=random.choice(consts.width)
        if grid[x][y]=='EMPTY' or  grid[x][y]=='mine':
            grid[x][y]='grass'
    return grid
def mines(grid):
    for i in range(20):
        x = random.choice(consts.height)
        y = random.choice(consts.width)
        if grid[x][y] == 'EMPTY' or grid[x][y]= 'grass':
            grid[x][y]='mine'
    return grid

create_screen()
grass(grid)
mines(grid)
for row in range(25):
    print(grid[row])
