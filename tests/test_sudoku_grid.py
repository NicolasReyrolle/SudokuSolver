"""Tests for SudokuGrid class."""
import unittest

from sudoku_grid import SudokuGrid


class SudokuGridTest(unittest.TestCase):
    """Test cases for SudokuGrid class."""

    def setUp(self):
        self.g = SudokuGrid()
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
        self.g.load(grid)

    def test_value_is_already_present(self):
        """Test that a value already present is not possible."""
        self.assertFalse(self.g.is_possible(0, 0, 4))

    def test_in_line_is_false(self):
        """Test that a value in the same line is not possible."""
        self.assertFalse(self.g.is_possible(1, 0, 9))

    def test_in_line_is_true(self):
        """Test that a value not in the line is possible."""
        self.assertTrue(self.g.is_possible(1, 0, 5))

    def test_in_column_is_false(self):
        """Test that a value in the same column is not possible."""
        self.assertFalse(self.g.is_possible(0, 1, 5))

    def test_in_column_is_true(self):
        """Test that a value not in the column is possible."""
        self.assertTrue(self.g.is_possible(0, 1, 6))

    def test_in_square_is_true(self):
        """Test that a value not in the square is possible."""
        self.assertTrue(self.g.is_possible(1, 1, 2))

    def test_in_square_is_false(self):
        """Test that a value in the same square is not possible."""
        self.assertFalse(self.g.is_possible(1, 1, 3))

    def test_base_printing(self):
        """Test that printing doesn't raise an exception."""
        self.g.print()

if __name__ == '__main__':
    unittest.main()
