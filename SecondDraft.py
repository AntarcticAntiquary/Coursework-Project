import pygame as pg
import random as r

# Set window properties
WIDTH = 500
HEIGHT = 500
CELLSIZE = 250

# Colours
RED = (200, 0, 0) # debug colour
BLACK = (0, 0, 0)
WATER = (0, 163, 225)
DIRT = (116, 102, 59)
PATH = (128, 126, 120)
GRASS = (0, 154, 23)
SAND = (241, 235, 156)

# Input (soil types) - soil type and water absorbed needed to waterlog it
soiltypes = {'sand': 12,
             'pebbles': 10,
             'path': 6,
             'dirt': 25,
             'loam': 30,
             'grass': 40,}
soiltypeslist = ['grass', 'dirt', 'path', 'sand']
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

def setup_grid(): # function to set up grid
    global cells
    for x in range(0, WIDTH, CELLSIZE):
        cellx = x // CELLSIZE # cellx/celly are different to x and y b/c column #1 may be at screen pos 10
        cells.insert(cellx, [])
        for y in range(0, HEIGHT, CELLSIZE):
            celly = y // CELLSIZE
            cells[cellx].insert(celly, sample_cell)
            currentcell = cells[cellx][celly]
            print(currentcell)
            rect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
            pg.draw.rect(screen, RED, rect, 0)
            currentcell['soiltype'] = r.choice(soiltypeslist)
            print(currentcell['soiltype'], cellx, celly)
            print()
            for l in cells:
                for cell in l:
                    print(cell['soiltype'])
            
def update_grid():
    for x in range(0, WIDTH, CELLSIZE):
        cellx = x // CELLSIZE
        for y in range(0, HEIGHT, CELLSIZE):
            celly = y // CELLSIZE
            cell = cells[cellx][celly]
            colour = RED
            if cell['waterlevels'] > 0:
                colour = WATER
            elif cell['soiltype'] == 'dirt':
                colour = DIRT
            elif cell['soiltype'] == 'path':
                colour = PATH
            elif cell['soiltype'] == 'grass':
                colour = GRASS
            elif cell['soiltype'] == 'sand':
                colour = SAND
            rect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
            pg.draw.rect(screen, colour, rect, 0)
    pg.display.update()
            
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
            cell = y
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
setup_grid()
pg.display.update()

for l in cells:
    for cell in l:
        print(cell['soiltype'])
update_grid()

running = True

# print()
# print(cells)

while running:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
                pg.quit()
            elif event.key == pg.K_t:
                tick_passes()
                update_grid()
                print(cells[0][0])
