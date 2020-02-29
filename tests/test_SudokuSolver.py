import unittest

from .context import SudokuSolver


class SudokuSolverTest(unittest.TestCase):
    s = SudokuSolver()

    def setUp(self):
        grid = [
            [4, 0, 0, 0, 0, 5, 0, 0, 0],
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

    def test_value_is_already_present(self):
        self.assertFalse(self.s.is_possible(0, 0, 4))

    def test_in_line_is_true(self):
        self.assertTrue(self.s.is_possible(1, 0, 9))

    def test_in_line_is_false(self):
        self.assertFalse(self.s.is_possible(1, 0, 5))

    def test_in_column_is_true(self):
        self.assertTrue(self.s.is_possible(0, 1, 5))

    def test_in_column_is_false(self):
        self.assertFalse(self.s.is_possible(0, 1, 6))

    def test_in_square_is_true(self):
        self.assertTrue(self.s.is_possible(1, 1, 2))

    def test_in_square_is_false(self):
        self.assertFalse(self.s.is_possible(1, 1, 3))

if __name__ == '__main__':
    unittest.main()
