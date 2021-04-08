from main import get_applicable_moves, get_empty_slots, goal_test, is_valid

losing_board = [
    [None, None, None, 1, 1, 1, None, None, None],
    [None, None, None, 1, 1, 1, None, None, None],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [None, None, None, 1, 1, 1, None, None, None],
    [None, None, None, 1, 1, 1, None, None, None]
]

winning_board = [
    [None, None, None, 0, 0, 0, None, None, None],
    [None, None, None, 0, 0, 0, None, None, None],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, ],
    [None, None, None, 0, 0, 0, None, None, None],
    [None, None, None, 0, 0, 0, None, None, None]
]


def test_goal_test_win():
    assert goal_test(winning_board) is True


def test_goal_test_lose():
    assert goal_test(losing_board) is False


def test_is_valid():
    assert is_valid([[1, 1, 0]], (0, 0), (1, 0), (2, 0))


def test_applicable_moves():
    board = [[None, None, 0, 0, 1, None, None],
             [None, None, 0, 0, 1, None, None],
             [1, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [None, None, 0, 0, 0, None, None],
             [None, None, 1, 1, 1, None, None]]
    empty_slots = get_empty_slots(board)
    print(empty_slots)
    assert get_applicable_moves(board, empty_slots) == True