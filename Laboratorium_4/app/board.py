from .utils import get_randomised_position, clear_console
import random

class Board:
    EMPTY = '.'
    FINISH = 'B'
    OBSTACLE = 'X'

    def __init__(self, size: int, player_pos: tuple, num_obstacles: int):
        self.size = size
        self.content = [[self.EMPTY for _ in range(self.size)] for _ in range(self.size)]
        self.player_pos = player_pos
        self.update_player_pos(player_pos)
        self.finish_pos = self.generate_finish()
        self.generate_obstacles(num_obstacles)

    def __str__(self):
        return "\n".join([" ".join(row) for row in self.content])

    def generate_obstacles(self, num_obstacles):
        for _ in range(num_obstacles):
            obstacle_pos = self.get_randomised_obstacle_position()
            while obstacle_pos == self.player_pos or obstacle_pos == self.finish_pos or self.is_obstacle(obstacle_pos):
                obstacle_pos = self.get_randomised_obstacle_position()
            self.content[obstacle_pos[0]][obstacle_pos[1]] = self.OBSTACLE

    def get_randomised_obstacle_position(self):
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1)

    def is_obstacle(self, pos):
        return self.content[pos[0]][pos[1]] == self.OBSTACLE

    def generate_finish(self):
        finish_pos = get_randomised_position(self.size)
        while self.is_adjacent(finish_pos, self.player_pos):
            finish_pos = get_randomised_position(self.size)
        self.content[finish_pos[0]][finish_pos[1]] = self.FINISH
        return finish_pos

    def is_finish(self, pos):
        return pos == self.finish_pos

    def is_adjacent(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1

    def update_player_pos(self, new_player_pos: tuple):
        self.content[self.player_pos[0]][self.player_pos[1]] = self.EMPTY
        self.player_pos = new_player_pos
        self.content[self.player_pos[0]][self.player_pos[1]] = 'A'

    def draw(self):
        clear_console()
        print(self.__str__())
