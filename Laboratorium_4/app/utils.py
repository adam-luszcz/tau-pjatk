import random
from enum import Enum
from os import system, name

class Directions(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


def get_randomised_position(board_size: int):
    last_idx = board_size - 1
    border_choice = random.choice(['top', 'bottom', 'left', 'right'])

    if border_choice in ['top', 'bottom']:
        x = 0 if border_choice == 'top' else last_idx
        y = random.randint(0, last_idx)
    else:
        y = 0 if border_choice == 'left' else last_idx
        x = random.randint(0, last_idx)

    return x, y


def clear_console():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
