import pygame as pg
import time as t
import random as r

# Set window properties
WIDTH = 500
HEIGHT = 500
CELLSIZE = 50

# Colours
RED = (200, 0, 0) 
BLACK = (0, 0, 0)

# Input (soil types) - soil type and water absorbed needed to waterlog it
soiltypes = {'sand': 12,
             'pebbles': 10
             'path': 6
             'dirt': 25
             'loam': 30
             'grass': 40}

# Initialise cell properties list
cells = []
sample_cell = {'altitude': 50, # set properties for each cell
               'obstructed': False,
               'waterlogged': False,
               'waterlevels': 0,
               'waterabsorbed': 0,
               'soiltype': 'dirt',}
#                'x': 0,
#                'y': 0,}
precipitation = 5
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)

def draw_grid(): # function to set up grid
    for x in range(0, WIDTH, CELLSIZE):
        cellx = x // CELLSIZE # cellx/celly are different to x and y b/c column #1 may be at screen pos 10
        cells.insert(cellx, [])
        for y in range(0, HEIGHT, CELLSIZE):
            celly = y // CELLSIZE
            cells[cellx].insert(celly, sample_cell)
            rect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
            pg.draw.rect(screen, RED, rect, 1)
            
def get_adjacent_coords(x, y): # Function to find the adjacent coords to a given coordinate
    adjacencies = []
    adjacencies.append(x+1, y)
    adjacencies.append(x-1, y)
    adjacencies.append(x, y+1)
    adjacencies.append(x, y-1)
    return adjacencies

def tick_passes():
    global cells
    for x in cells:
        for y in x:
            cell = cells[x][y]
            rain = precipitation
            soiltype = cell['soiltype']
            if cell['obstructed']:
                rain = round(0.8 * rain)
            if cell['waterlogged']:
                cell['waterlevels'] += rain
            else:
                cell['waterabsorbed'] += rain
                if cell['waterabsorbed'] >= soiltypes[soiltype]:
                    cell['waterlogged'] = True
draw_grid()
pg.display.update()

running = True

print()
print(cells)

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
                pg.quit()
