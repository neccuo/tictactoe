import utils as utl
import tictactoe as ttt

def evaluate_state(GRID, tile):
    return utl.game_result(GRID, tile)

def init_dic(dc, keys, val=0):
    for key in keys:
        dc[key] = val
    return dc

def main(GRID, tile, depth=1):
    # comeback here
    actions = utl.get_possible_actions(GRID)
    my_dic = init_dic({}, actions, 0)
    
    for action in actions:
        tempGRID = ttt.foresee_grid(GRID, action, tile)
        my_dic[action] = utl.game_result(tempGRID, tile)