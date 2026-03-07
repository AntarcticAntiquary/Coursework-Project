# Algorithm for data conversion:

# Needed format:
# {'dirt': 25, 'grass': 40}

# Input format:
sample_input = [[0, 1, 0], [0, 2, 191], [0, 3, 476], [0, 4, 798], [0, 5, 910], [1, 1, 0]]

waterlogged_level = 825

soiltypes = {
    'dirt': 0,
    'grass': 0,
    'pebbles': 0,
    'mulch': 0,
    }

for datapoint in sample_input:
    currentpot = datapoint[0]
    if currentpot == 0:
        currentpot = 'dirt'
    elif currentpot == 1:
        currentpot = 'grass'
    elif currentpot == 2:
        currentpot = 'pebbles'
    elif currentpot == 3:
        currentpot = 'mulch'
    wateradded = datapoint[1]
    moisturelevel = datapoint[2]
    if moisturelevel > waterlogged_level:
        soiltypes[currentpot] = wateradded
        
print(soiltypes)
