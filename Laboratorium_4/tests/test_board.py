import unittest
from Laboratorium_4.app.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.player_pos = (0, 0)
        self.num_obstacles = 3
        self.board = Board(self.size, self.player_pos, self.num_obstacles)

    def test_initialization(self):
        self.assertEqual(self.board.size, self.size)
        self.assertIsNotNone(self.board.content)
        self.assertEqual(len(self.board.content), self.size)

    def test_player_initial_position(self):
        self.assertEqual(self.board.player_pos, self.player_pos)
        self.assertEqual(self.board.content[self.player_pos[0]][self.player_pos[1]], 'A')

    def test_finish_position(self):
        finish_x, finish_y = self.board.finish_pos
        self.assertEqual(self.board.content[finish_x][finish_y], self.board.FINISH)

    def test_obstacle_count(self):
        obstacle_count = sum(row.count(self.board.OBSTACLE) for row in self.board.content)
        self.assertEqual(obstacle_count, self.num_obstacles)

    def test_update_player_position(self):
        new_player_pos = (1, 1)
        self.board.update_player_pos(new_player_pos)
        self.assertEqual(self.board.player_pos, new_player_pos)
        self.assertEqual(self.board.content[new_player_pos[0]][new_player_pos[1]], 'A')


if __name__ == '__main__':
    unittest.main()
