import unittest

from SudokuGrid import SudokuGrid


class SudokuGridTest(unittest.TestCase):
    g = SudokuGrid()

    def setUp(self):
        grid = [
            [4, 0, 0, 0, 9, 5, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 1, 9, 8],
            [3, 0, 0, 0, 7, 2, 4, 0, 0],
            [0, 0, 0, 1, 2, 0, 0, 8, 0],
            [9, 8, 7, 6, 5, 4, 3, 2, 0],
            [0, 0, 0, 0, 3, 0, 6, 7, 0],
            [0, 5, 0, 0, 6, 9, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 9, 0, 7],
            [6, 4, 0, 3, 8, 0, 0, 0, 0],
        ]
        self.g.load(grid)

    def test_get_value_at(self):
        self.assertEqual(6, self.g.get_value_at(8, 0))

    def test_set_value_at(self):
        self.g.set_value_at(0, 0, 9)
        self.assertEqual(9, self.g.get_value_at(0, 0))
        self.g.set_value_at(0, 0, 4)
        self.assertEqual(4, self.g.get_value_at(0, 0))

    def test_get_value_at2(self):
        self.assertEqual(7, self.g.get_value_at(7, 8))

    def test_value_is_already_present(self):
        self.assertFalse(self.g.is_possible(0, 0, 4))

    def test_value_is_already_present2(self):
        self.assertFalse(self.g.is_possible(8, 0, 2))

    def test_in_line_is_true(self):
        self.assertTrue(self.g.is_possible(1, 0, 2))

    def test_in_line_is_false(self):
        self.assertFalse(self.g.is_possible(1, 0, 9))

    def test_in_column_is_true(self):
        self.assertTrue(self.g.is_possible(0, 1, 2))

    def test_in_column_is_false(self):
        self.assertFalse(self.g.is_possible(0, 1, 4))

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

    def test_count_possible_values_zero(self):
        self.assertEqual(0, self.g.count_possible_values(0, 0))

    def test_count_possible_values_three(self):
        self.assertEqual(3, self.g.count_possible_values(1, 0))

    def test_count_possible_values_four(self):
        self.assertEqual(4, self.g.count_possible_values(0, 1))

    def test_count_possible_values_one(self):
        self.assertEqual(1, self.g.count_possible_values(4, 8))

    def test_solve_single_possibility(self):
        self.assertEqual(7, self.g.solve_single_possibility())
        self.assertEqual(1, self.g.get_value_at(4, 8))

    def test_get_first_possible_value(self):
        self.assertEqual(1, self.g.get_first_possible_value(4, 8))

    def test_get_first_possible_value_already_present(self):
        self.assertEqual(4, self.g.get_first_possible_value(0, 0))


if __name__ == '__main__':
    unittest.main()
