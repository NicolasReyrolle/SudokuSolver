import unittest

from sudoku_grid import SudokuGrid


class SudokuGridTestSolveFailure(unittest.TestCase):
    """Test a simple column resolution"""
    g = SudokuGrid()

    def setUp(self):
        grid = [
            [0, 7, 0, 5, 0, 3, 4, 8, 0],
            [0, 3, 0, 6, 0, 0, 7, 0, 2],
            [0, 0, 0, 8, 7, 0, 0, 1, 6],
            [0, 5, 0, 0, 6, 9, 2, 0, 8],
            [0, 9, 0, 2, 0, 0, 5, 0, 7],
            [4, 0, 0, 0, 0, 0, 0, 0, 1],
            [8, 0, 0, 0, 4, 7, 1, 0, 5],
            [3, 6, 7, 0, 0, 8, 9, 0, 4],
            [0, 0, 4, 0, 2, 0, 0, 0, 3],
        ]
        self.g.load(grid)

    def test_column_resolution(self):
        self.g.solve_cell(3, 7)
        self.assertNotEqual(self.g.get_value_at(3, 7), 9)

    def test_column_resolution2(self):
        self.g.set_value_at(0, 8, 9)
        self.g.solve_cell(1, 7)
        self.assertNotEqual(self.g.get_value_at(1, 7), 9)

if __name__ == '__main__':
    unittest.main()
