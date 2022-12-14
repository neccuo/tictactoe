import random
from enum import Enum
from utils import *

class State(Enum): # UNUSED
    CONT = 0
    PX_W = 1
    PO_W = 2
    DRAW = 3

GRID = \
[
    [Tile.N,Tile.N,Tile.N],
    [Tile.N,Tile.N,Tile.N],
    [Tile.N,Tile.N,Tile.N]
]
        
def play(GRID, x, y, tile):
    if not is_action_legal(GRID, (x, y)):
        return False
    GRID[y][x] = tile
    return True

def play(GRID, action, tile):
    x = action[0]
    y = action[1]
    play(GRID, x, y, tile)
    
def foresee_grid(GRID, action, tile): # play and return next state without modifying the original
    copyGRID = GRID[::]
    play(copyGRID, action, tile)
    return copyGRID

def player_turn(GRID, tile):
    coor = input("enter coor: ")
    if coor == "s": # backdoor
        return True
    int_inps = [int(x) for x in coor.split(' ')]
    x = int_inps[0]
    y = int_inps[1]
    if not play(GRID, x, y, tile):
        print("Action is not legal")
        return False
    return True

def random_turn(GRID, tile):
    legal_actions = get_possible_actions(GRID)
    c = len(legal_actions)
    act = random.randint(0, c-1)
    coo = legal_actions[act]
    play(GRID, coo[0], coo[1], tile)

def pl_v_rand(GRID):
    turn = 1
    tile = Tile.X
    while not check_end(GRID, tile):
        print_grid(GRID)
        if turn == 1:
            tile = Tile.X
            if player_turn(GRID, tile) == False:
                continue
        else:
            tile = Tile.O
            random_turn(GRID, tile)
        turn *= -1
    print_grid(GRID)
    # print('Player[' + tile.value + '] won')

pl_v_rand(GRID)