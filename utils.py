from enum import Enum

class Tile(Enum):
    N = " "
    X = "X"
    O = "O"

def check_cols(GRID, tile):
    ln = len(GRID)
    for i in range(ln):
        arr = []
        for j in range(ln):
            arr.append(GRID[j][i])
        if is_arr_same(arr, tile):
            return True
    return False

def check_rows(GRID, tile):
    for row in GRID:
        if is_arr_same(row, tile):
            return True
    return False

def check_diags(GRID, tile):
    ln = len(GRID)
    arr1 = []
    arr2 = []
    for i in range(ln):
        arr1.append(GRID[i][i])
        arr2.append(GRID[i][ln-1-i])
    if is_arr_same(arr1, tile) or is_arr_same(arr2, tile):
        return True
    return False

def check_winlose(GRID, tile):
    if  check_cols(GRID, tile) or \
        check_rows(GRID, tile) or \
        check_diags(GRID, tile):
        return True
    return False

def check_draw(GRID):
    return len(get_possible_actions(GRID)) == 0

def check_end(GRID, tile):
    # GRID[Y][X]
    if  check_winlose(GRID, tile) or \
        check_draw(GRID):
        return True
    return False

def negate_tile(tile):
    if tile == Tile.N:
        raise Exception("null tile cannot be negated")
    if tile == Tile.X:
        opp = Tile.O
    else:
        opp = Tile.X
        
    return opp

def game_result(GRID, tile):
    opp = negate_tile(tile)
        
    if check_winlose(GRID, tile):
        return 1
    elif check_winlose(GRID, opp):
        return -1
    else: # continue or draw
        return 0
            
def is_arr_same(arr, tile=Tile.X):
    temp = tile
    for elem in arr:
        if elem == Tile.N or elem != temp:
            return False
        temp = elem
    return True

def print_grid(GRID):
    for row in GRID:
        arr = []
        for elem in row:
            arr.append(elem.value) 
        print(arr)
    print()
    
def get_possible_actions(GRID):
    ln = len(GRID)
    arr = []
    for i in range(ln):
        for j in range(ln):
            tile = GRID[j][i]
            if tile == Tile.N:
                arr.append((i, j))
    return arr

def is_action_legal(GRID, action):
    legal_actions = get_possible_actions(GRID)
    if (action[0], action[1]) not in legal_actions:
        return False
    return True