from board import Board
from player import Player
from pynput import keyboard
from utils import Directions

class Game:
    BOARD_SIZE = 5
    NUM_OBSTACLES = 3

    def __init__(self):
        self.player = Player(self.BOARD_SIZE)
        self.board = Board(self.BOARD_SIZE, (self.player.x, self.player.y), self.NUM_OBSTACLES)

    def on_press(self, key):
        direction_map = {
            keyboard.Key.right: Directions.RIGHT,
            keyboard.Key.left: Directions.LEFT,
            keyboard.Key.up: Directions.UP,
            keyboard.Key.down: Directions.DOWN
        }

        if key in direction_map:
            self.update_game(direction_map[key])
        elif key == keyboard.Key.esc:
            exit()

    def update_game(self, direction):
        self.player.move_player(direction=direction)
        new_pos = (self.player.x, self.player.y)

        if self.board.is_obstacle(new_pos):
            print("Game over!")
            exit()

        if self.board.is_finish(new_pos):
            print("Congratulations! You've reached the finish!")
            exit()

        self.board.update_player_pos(new_pos)
        self.board.draw()

if __name__ == '__main__':
    game = Game()
    game.board.draw()

    with keyboard.Listener(on_release=game.on_press) as listener:
        listener.join()
