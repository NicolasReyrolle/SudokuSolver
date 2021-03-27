import unittest

from SudokuSolver import SudokuSolver


class SudokuSolverTestFirstIssue(unittest.TestCase):
    s = SudokuSolver()

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
        self.s.load_grid(grid)

    def test_is_false(self):
        self.assertFalse(self.s.is_possible(4, 0, 2))


if __name__ == '__main__':
    unittest.main()
