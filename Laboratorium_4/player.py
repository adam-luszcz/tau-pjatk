from utils import get_randomised_position, Directions

class Player:
    def __init__(self, board_size: int):
        self.board_size = board_size
        self.x, self.y = get_randomised_position(self.board_size)

    def move_player(self, direction: Directions):
        delta = {
            Directions.UP: (-1, 0),
            Directions.DOWN: (1, 0),
            Directions.LEFT: (0, -1),
            Directions.RIGHT: (0, 1)
        }

        dx, dy = delta[direction]
        new_x, new_y = self.x + dx, self.y + dy

        if 0 <= new_x < self.board_size:
            self.x = new_x
        if 0 <= new_y < self.board_size:
            self.y = new_y
