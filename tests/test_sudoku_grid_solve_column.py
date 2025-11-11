import unittest

from sudoku_grid import SudokuGrid


class SudokuGridTestSolveColumn(unittest.TestCase):
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

    def test_simple_resolution(self):
        self.assertTrue(self.g.solve_cell(0, 8))
        self.assertEqual(self.g.get_value_at(0, 8), 9)

    def test_cannot_resolve(self):
        self.assertFalse(self.g.solve_cell(0, 0))
        self.assertEqual(self.g.get_value_at(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
