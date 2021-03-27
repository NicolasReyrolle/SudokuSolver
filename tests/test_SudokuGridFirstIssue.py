import unittest

from SudokuGrid import SudokuGrid


class SudokuGridTestFirstIssue(unittest.TestCase):
    g = SudokuGrid()

    def setUp(self):
        grid = [
            [4, 2, 1, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 9, 8],
            [3, 0, 0, 0, 8, 2, 4, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 8, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 6, 7, 0],
            [0, 5, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 9, 0, 7],
            [6, 4, 0, 3, 0, 0, 0, 0, 0],
        ]
        self.g.load(grid)

    def test_is_false(self):
        self.assertFalse(self.g.is_possible(4, 0, 2))


if __name__ == '__main__':
    unittest.main()
