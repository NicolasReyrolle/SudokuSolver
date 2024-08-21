import unittest

from SudokuGrid import SudokuGrid


class SudokuGridTestSolveSimpleProblem(unittest.TestCase):
    g = SudokuGrid()

    def setUp(self):
        grid = [
            [0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 3, 0, 6, 0, 0, 7, 0, 2],
            [0, 0, 0, 8, 7, 0, 0, 1, 6],
            [0, 5, 0, 0, 6, 9, 2, 0, 8],
            [0, 9, 0, 2, 0, 0, 5, 0, 7],
            [4, 0, 0, 0, 0, 0, 0, 0, 1],
            [8, 0, 0, 0, 4, 7, 1, 0, 5],
            [3, 6, 7, 0, 0, 8, 0, 0, 4],
            [0, 0, 4, 0, 2, 0, 0, 0, 3],
        ]
        self.g.load(grid)

    def test_resolution(self):
        self.g.solve()
        self.assertTrue(self.g.is_solved())

if __name__ == '__main__':
    unittest.main()
