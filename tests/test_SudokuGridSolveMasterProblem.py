import unittest

from SudokuGrid import SudokuGrid


class SudokuGridTestSolveComplexProblem(unittest.TestCase):
    g = SudokuGrid()

    def setUp(self):
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [6, 0, 0, 4, 2, 0, 0, 0, 0],
            [0, 0, 4, 9, 0, 1, 0, 0, 3],
            [0, 0, 0, 0, 0, 9, 7, 0, 0],
            [0, 0, 6, 0, 0, 8, 4, 0, 0],
            [8, 9, 1, 0, 0, 4, 0, 0, 0],
            [0, 0, 9, 0, 5, 6, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 8],
            [5, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        self.g.load(grid)

    def test_resolution(self):
        self.g.solve()
        self.assertTrue(self.g.is_solved())
        self.assertNotEqual(self.g.get_value_at(3, 7), 9)

if __name__ == '__main__':
    unittest.main()
