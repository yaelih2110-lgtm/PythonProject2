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
        if grid[x][y] == ['EMPTY']:
            grid[x][y]=['mine']
    return grid
def print_grid(grid):
    create_screen()
    mines(grid)
    for row in range(25):
        print(grid[row])
print_grid(grid)
