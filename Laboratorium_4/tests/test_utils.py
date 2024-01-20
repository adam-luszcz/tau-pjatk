import unittest
from Laboratorium_4.app.utils import *

class TestUtils(unittest.TestCase):
    def test_get_randomised_position(self):
        board_size = 5
        for _ in range(100):
            x, y = get_randomised_position(board_size)
            self.assertTrue(0 <= x < board_size and 0 <= y < board_size)
            self.assertTrue(x == 0 or x == board_size - 1 or y == 0 or y == board_size - 1)


if __name__ == '__main__':
    unittest.main()
