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

def mines(grid):
    for i in range(20):
        x = random.choice(range(consts.height))
        y = random.choice(range(consts.width))
        if (grid[x][y] == ['EMPTY'] and grid[x][y+1]==['EMPTY'] and grid[x][y+2]==['EMPTY'] and grid[x][y] != grid[0][0]
                and grid[x][y] != grid[0][1] and grid[x][y] != grid[1][0] and grid[x][y] != grid[1][1] and grid[x][y] != grid[2][0]
                and grid[x][y] != grid[2][1] and grid[x][y] != grid[3][0] and grid[x][y] != grid[3][1] and grid[x][y] != grid[4][0] and grid[x][y] != grid[4][1]):
            grid[x][y]='mine'
            grid[x][y-1]='mine'
            grid[x][y+1]='mine'
    return grid
def print_grid(grid):
    create_screen()
    mines(grid)
    for row in range(25):
        print(grid[row])
print_grid(grid)
def soldier_initial_place(grid):
    grid[0][0]='soldier_initial_place'
    grid[0][1]='soldier_initial_place'
    grid[1][0]='soldier_initial_place'
    grid[1][1]='soldier_initial_place'
    grid[2][0]='soldier_initial_place'
    grid[2][1]='soldier_initial_place'
    grid[3][0]='soldier_initial_place'
    grid[3][1]='soldier_initial_place'
    grid[4][0]='soldier_initial_place'
    grid[4][1]='soldier_initial_place'

