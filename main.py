# Todo:
#  Make an array representing all possible states
#  Create function which checks the goal start
#  Limit the states to applicable actions
#  Visualise each step
#  Make it do it once slowly and then fail
#  Version control it and time each iteration?
#  Add path cost, could be inverse distance from the center?
#  add rollback
#  implement basic caching
from copy import deepcopy
from pprint import pprint


class Board(list):
    def __init__(self, *args):
        list.__init__(self, deepcopy(START_BOARD))


START_BOARD = [
    [None, None, 1, 1, 1, None, None],
    [None, None, 1, 1, 1, None, None],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [None, None, 1, 1, 1, None, None],
    [None, None, 1, 1, 1, None, None]
]


def goal_test(board):
    if board[3][3] == 0:
        return False
    t_board = deepcopy(board)
    t_board[3].pop(3)
    for row in t_board:
        if any(row):
            return False
    return True


def get_applicable_states(board):
    applicable_moves = []
    empty_slots = []
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            if value == 0 and is_valid(board, to=(x, y)):
                empty_slots.append((x, y))

    for x, y in empty_slots:
        to = x, y
        if y > 1:
            from_ = x, y - 2
            remove = x, y - 1
            if remove not in empty_slots and is_valid(board, from_, remove, to):
                applicable_moves.append((from_, remove, to))

        if x > 1:
            from_ = x - 2, y
            remove = x - 1, y
            if remove not in empty_slots and is_valid(board, from_, remove, to):
                applicable_moves.append((from_, remove, to))

        if y < 5:
            from_ = x, y + 2
            remove = x, y + 1
            if remove not in empty_slots and is_valid(board, from_, remove, to):
                applicable_moves.append((from_, remove, to))

        if x < 5:
            from_ = x + 2, y
            remove = x + 1, y
            if remove not in empty_slots and is_valid(board, from_, remove, to):
                applicable_moves.append((from_, remove, to))

    for move in applicable_moves:
        t_board = apply_move(move, board)
        if goal_test(t_board):
            print("winner")
            return t_board
        display_board(t_board)
        return get_applicable_states(t_board)
    else:

        print("time to backtrack")

def is_valid(board, from_=None, remove=None, to=None):
    try:
        if from_ is not None:
            x, y = from_
            if not board[y][x]:
                return False
        if remove is not None:
            x, y = remove
            if not board[y][x]:
                return False
        if to is not None:
            x, y = to
            return board[y][x] == 0
        return True
    except Exception as e:
        print(board)
        raise



def display_board(board):
    for row in board:
        for position in row:
            if position is None:
                print("  ", end="")
            elif position == 1:
                print("\u2b24", end="")
            elif position == 0:
                print("\u2b55", end="")
            else:
                raise Exception("HOWS?", position)
        print()
    print()

def apply_move(move, board):
    t_board = deepcopy(board)
    (from_x, from_y), (remove_x, remove_y), (to_x, to_y) = move
    assert t_board[from_y][from_x] == 1
    assert t_board[remove_y][remove_x] == 1
    assert t_board[to_y][to_x] == 0
    t_board[from_y][from_x] = 0
    t_board[remove_y][remove_x] = 0
    t_board[to_y][to_x] = 1

    return t_board


if __name__ == '__main__':
    display_board(START_BOARD)
    print(get_applicable_states(START_BOARD))



