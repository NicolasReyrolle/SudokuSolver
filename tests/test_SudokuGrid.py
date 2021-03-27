import unittest

from SudokuGrid import SudokuGrid


class SudokuGridTest(unittest.TestCase):
    g = SudokuGrid()

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
        self.g.load(grid)

    def test_value_is_already_present(self):
        self.assertFalse(self.g.is_possible(0, 0, 4))

    def test_in_line_is_true(self):
        self.assertTrue(self.g.is_possible(1, 0, 9))

    def test_in_line_is_false(self):
        self.assertFalse(self.g.is_possible(1, 0, 5))

    def test_in_column_is_true(self):
        self.assertTrue(self.g.is_possible(0, 1, 5))

    def test_in_column_is_false(self):
        self.assertFalse(self.g.is_possible(0, 1, 6))

    def test_in_square_is_true(self):
        self.assertTrue(self.g.is_possible(1, 1, 2))

    def test_in_square_is_false(self):
        self.assertFalse(self.g.is_possible(1, 1, 3))

    def test_base_printing(self):
        raised = False
        try:
            self.g.print()
        except:
            raised = True

        self.assertFalse(raised, "Printing should not raise an exception")


if __name__ == '__main__':
    unittest.main()
