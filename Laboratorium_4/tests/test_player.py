import unittest
from unittest.mock import patch
from Laboratorium_4.app.player import Player
from Laboratorium_4.app.utils import Directions


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.board_size = 5
        with patch('Laboratorium_4.app.player.get_randomised_position', return_value=(2, 2)):
            self.player = Player(self.board_size)

    def test_initialization(self):
        self.assertEqual(self.player.board_size, self.board_size)
        self.assertEqual((self.player.x, self.player.y), (2, 2))

    def test_move_up_within_bounds(self):
        self.player.move_player(Directions.UP)
        self.assertEqual(self.player.x, 1)
        self.assertEqual(self.player.y, 2)

    def test_move_down_within_bounds(self):
        self.player.move_player(Directions.DOWN)
        self.assertEqual(self.player.x, 3)
        self.assertEqual(self.player.y, 2)

    def test_move_left_boundary(self):
        self.player.x, self.player.y = 0, 0
        self.player.move_player(Directions.LEFT)
        self.assertEqual(self.player.x, 0)
        self.assertEqual(self.player.y, 0)

    def test_move_right_boundary(self):
        self.player.x, self.player.y = self.board_size - 1, self.board_size - 1
        self.player.move_player(Directions.RIGHT)
        self.assertEqual(self.player.x, self.board_size - 1)
        self.assertEqual(self.player.y, self.board_size - 1)


if __name__ == '__main__':
    unittest.main()
