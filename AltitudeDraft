import pygame as pg
import random as r

# Set which scenario we are considering
scenario = 3

# Set window properties
LENGTH = 15
CELLSIZE = 25
WIDTH = LENGTH * CELLSIZE
HEIGHT = LENGTH * CELLSIZE

# Colours
RED = (200, 0, 0) # debug colour
BLACK = (0, 0, 0)
WATER = (0, 163, 225)
DIRT = (116, 102, 59)
PATH = (128, 126, 120)
GRASS = (0, 154, 23)
SAND = (241, 235, 156)
ALT1 = (-40, -40, -40)
ALT2 = (-20, -20, -20)
ALT3 = (0, 0, 0)
ALT4 = (20, 20, 20)
ALT5 = (40, 40, 40)

preset_map_path = [ # A preset map for scenarios, if we want to use it
    ['G', 'G', 'G', 'P', 'P', 'P', 'D', 'G', 'G', 'D', 'G', 'S', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'P', 'P', 'P', 'D', 'G', 'D', 'G', 'G', 'S', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'G', 'P', 'P', 'P', 'G', 'G', 'D', 'D', 'S', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'D', 'P', 'P', 'P', 'G', 'G', 'G', 'D', 'S', 'S', 'S', 'S',],
    ['G', 'G', 'D', 'G', 'P', 'P', 'P', 'G', 'D', 'D', 'D', 'S', 'S', 'S', 'S',],
    ['G', 'G', 'D', 'G', 'P', 'P', 'P', 'G', 'G', 'G', 'G', 'D', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'G', 'D', 'P', 'P', 'P', 'G', 'D', 'G', 'G', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'G', 'D', 'P', 'P', 'P', 'G', 'G', 'G', 'D', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'G', 'D', 'P', 'P', 'P', 'G', 'D', 'G', 'G', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'G', 'D', 'P', 'P', 'P', 'G', 'G', 'D', 'G', 'S', 'S', 'S',],
    ['G', 'D', 'G', 'D', 'G', 'P', 'P', 'P', 'D', 'G', 'D', 'G', 'S', 'S', 'S',],
    ['G', 'G', 'G', 'G', 'G', 'P', 'P', 'P', 'G', 'D', 'D', 'D', 'S', 'S', 'S',],
    ['G', 'G', 'D', 'G', 'P', 'P', 'P', 'G', 'G', 'D', 'G', 'G', 'D', 'S', 'S',],
    ['G', 'G', 'D', 'D', 'P', 'P', 'P', 'D', 'G', 'G', 'G', 'D', 'G', 'S', 'S',],
    ['G', 'G', 'D', 'G', 'P', 'P', 'P', 'D', 'G', 'G', 'G', 'G', 'G', 'S', 'S',],
    ]

# Input (soil types) - soil type and water absorbed needed to waterlog it - this must be taken from microbit
soiltypes = {'S': 12,
             'P': 6,
             'D': 25,
             'G': 40,}
soiltypeslist = ['G', 'D', 'P', 'S']
# Initialise cell properties list
cells = []
precipitation = 5 # Set up various scenarios
if scenario == 2:
    precipitation = 2
elif scenario == 3:
    precipitation = 10
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
tick_counter = 0

def add_colours(colour1, colour2): # Function to add colours (to show changes in altitude)
    digit0 = colour1[0] + colour2[0]
    digit1 = colour1[1] + colour2[1]
    digit2 = colour1[2] + colour2[2]
    if digit0 > 255:
        digit0 = 255
    elif digit0 < 0:
        digit0 = 0
    if digit1 > 255:
        digit1 = 255
    elif digit1 < 0:
        digit1 = 0
    if digit2 > 255:
        digit2 = 255
    elif digit2 < 0:
        digit2 = 0
    result = (digit0, digit1, digit2)
    return result

def setup_cellist(): # Make the dictionary which will serve as the primary data structure
    global cells
    for x in range(LENGTH):
        cells.insert(x, [])
        for y in range(LENGTH):
            cells[x].insert(y, {})
            cells[x][y]['soiltype'] = 'D'
            cells[x][y]['waterlevels'] = 0
            cells[x][y]['obstructed'] = False
            cells[x][y]['waterlogged'] = False
            cells[x][y]['waterabsorbed'] = 0
            cells[x][y]['altitude'] = r.randint(1, 5)

def setup_grid(): # function to set up grid
    global cells
    setup_cellist()
    for x in range(0, WIDTH, CELLSIZE):
        cellx = x // CELLSIZE # cellx/celly are different to x and y b/c column #1 may be at screen pos 10
        for y in range(0, HEIGHT, CELLSIZE):
            celly = y // CELLSIZE
            currentcell = cells[cellx][celly]
            rect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
            pg.draw.rect(screen, RED, rect, 0)
            currentcell['soiltype'] = preset_map_path[cellx][celly]
            #currentcell['soiltype'] = r.choice(soiltypeslist) # choose a random soil type for this cell
            
def update_grid():
    for x in range(0, WIDTH, CELLSIZE):
        cellx = x // CELLSIZE
        for y in range(0, HEIGHT, CELLSIZE):
            celly = y // CELLSIZE # Find column/row number as distinct from screen pixel position
            cell = cells[cellx][celly]
            altitude = cell['altitude']
            colour = RED
            if cell['waterlevels'] > 0: # Choose appropriate colour
                colour = WATER
            elif cell['soiltype'] == 'D':
                colour = DIRT
            elif cell['soiltype'] == 'P':
                colour = PATH
            elif cell['soiltype'] == 'G':
                colour = GRASS
            elif cell['soiltype'] == 'S':
                colour = SAND
            if altitude == 1:
                colour = add_colours(colour, ALT1)
            elif altitude == 2:
                colour = add_colours(colour, ALT2)
            elif altitude == 3:
                colour = add_colours(colour, ALT3)
            elif altitude == 4:
                colour = add_colours(colour, ALT4)
            elif altitude == 5:
                colour = add_colours(colour, ALT5)
                
            rect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
            pg.draw.rect(screen, colour, rect, 0) # Draw cell
    pg.display.update() # Update pygame display
            
def get_adjacent_coords(x, y): # Function to find the adjacent coords to a given coordinate
    adjacencies = []           # Currently unused
    adjacencies.append(x+1, y)
    adjacencies.append(x-1, y)
    adjacencies.append(x, y+1)
    adjacencies.append(x, y-1)
    return adjacencies

def tick_passes(): # Add rainfall to each cell
    global cells
    global tick_counter
    tick_counter += 1 # So that we can tell the user how long it took to flood the area
    for x in cells:
        for y in x:
            cell = y
            rain = precipitation
            soiltype = cell['soiltype']
            if cell['obstructed']: # Functionality to handle tree coverage
                rain = round(0.8 * rain)
            if cell['waterlogged']: # Increase water levels above if the cell is waterlogged
                cell['waterlevels'] += rain
            else:
                cell['waterabsorbed'] += rain
                if cell['waterabsorbed'] >= soiltypes[soiltype]: # If the cell has reached capacity it is waterlogged
                    cell['waterlogged'] = True
                    
def check_flooded(): # Function that checks if the whole map is flooded
    flooded = True
    for x in cells:
        for y in x:
            if not y['waterlogged']: # If any cell is not flooded return false, else return true
                return False
    return True

setup_grid()
update_grid() # To show the initial stage of the map

running = True

while running: # Loop to check for events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False # If q is pressed, exit
                pg.quit()
            elif event.key == pg.K_t:
                tick_passes() # rain falls whenever the k t is pressed
                update_grid()
                if check_flooded(): # If the whole map is flooded
                    running = False
                    pg.quit()
                    print() # Tell the user how long it took to flood
                    print(f'It took {tick_counter} iterations to flood the map ({tick_counter*8}mm of rain)')
                    if tick_counter < 10:
                        print('There is a high risk of flooding for this area')
                    elif tick_counter > 20:
                        print('There is a low risk of flooding in this area')
                    else:
                        print('There is a moderate risk of flooding in this area')
