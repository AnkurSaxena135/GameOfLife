import pytest
import sys
from os import path

# putting this to provide easy of execution without much setup
sys.path.append(path.abspath(path.join(__file__, "..", "..")))

from game_of_life.game_of_life import GameOfLife

BOARD_SIZE = 10


@pytest.mark.parametrize(
    "init_state",
    [
        [(2, 2), (3, 3), (2, 3), (3, 2)],  # Square
        [(1, 2), (1, 3), (3, 2), (3, 3), (2, 1), (2, 4)],  # Beehive
        [(2, 2), (4, 2), (3, 1), (3, 3)],  # TUB
    ],
)
def test_still_lifes(init_state):
    board = GameOfLife(BOARD_SIZE, init_state)
    board.run(10)
    assert sorted(board.alive_cells) == sorted(init_state)


@pytest.mark.parametrize(
    "init_state, second_state",
    [
        ([(1, 2), (2, 2), (3, 2)], [(2, 1), (2, 2), (2, 3)]),  # line
        (
            [(1, 1), (1, 2), (2, 1), (4, 4), (4, 3), (3, 4)],
            [(1, 1), (1, 2), (2, 1), (4, 4), (4, 3), (3, 4), (2, 2), (3, 3)],
        ),  # beacon
    ],
)
def test_oscillators(init_state, second_state):

    for i in range(20):
        board = GameOfLife(BOARD_SIZE, init_state)
        board.run(i)
        if i % 2 == 1:
            assert sorted(board.alive_cells) == sorted(second_state)
        else:
            assert sorted(board.alive_cells) == sorted(init_state)


@pytest.mark.parametrize(
    "init_state, final_state",
    [
        (
            [(2, 2), (3, 3), (2, 3), (3, 2), (100, 0), (-1, -1)],
            [(2, 2), (3, 3), (2, 3), (3, 2)],
        ),
        (  # Square
            [(1, 2), (1, 3), (3, 2), (3, 3), (2, 1), (2, 4), (100, 0), (-1, -1)],
            [(1, 2), (1, 3), (3, 2), (3, 3), (2, 1), (2, 4)],
        ),  # Beehive
        (
            [(2, 2), (4, 2), (3, 1), (3, 3), (100, 0), (-1, -1)],  # TUB
            [(2, 2), (4, 2), (3, 1), (3, 3)],
        ),  # TUB
    ],
)
def test_out_of_bounds(init_state, final_state):

    board = GameOfLife(BOARD_SIZE, init_state)
    board.run(10)
    assert sorted(board.alive_cells) == sorted(final_state)
