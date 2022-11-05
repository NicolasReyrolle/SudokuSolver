from math import trunc


class SudokuGrid:
    grid = []

    def __init__(self):

        for rows in range(9):
            row = []
            for col in range(9):
                row.append(0)

    @staticmethod
    def print_frame_line():
        print(("*" + "-" * 7) * 3 + "*")

    def print(self):

        for i in range(9):
            self.print_line(i)

        self.print_frame_line()

    def print_line(self, i):
        if i % 3 == 0:
            self.print_frame_line()
        line = ""
        for j in range(9):
            line = self.print_column(i, j, line)
        print(line + "|")

    def print_column(self, i, j, line):
        if j % 3 == 0:
            line = line + "| "
        if self.grid[i][j] == 0:
            value = " "
        else:
            value = self.grid[i][j]
        line = line + str(value) + " "
        return line

    def load(self, sudoku_grid):
        self.grid = sudoku_grid

    def get_value_at(self, line: int, column: int):
        return self.grid[line][column]

    def is_possible(self, line: int, column: int, value: int) -> bool:
        # Check we do not already have the value
        if self.get_value_at(line, column) != 0:
            return False

        # Check the line
        for j in range(9):
            if self.get_value_at(line, j) == value:
                return False

        # Check the column
        for i in range(9):
            if self.get_value_at(i, column) == value:
                return False

        # Check the square
        square_line = trunc(line / 3)
        square_column = trunc(column / 3)
        for i in range(3):
            for j in range(3):
                if self.get_value_at(square_line * 3 + j, square_column * 3 + i) == value:
                    return False

        # Still there, we are good
        return True

    # Count the number of possible values in one box
    def count_possible_values(self, line: int, column: int):
        count = 0
        for n in range(9):
            if self.is_possible(line, column, n + 1):
                count = count + 1
        return count

    def solve(self):
        for x in range(9):
            self.solve_row(x)
        self.print()

    def solve_row(self, x):
        for y in range(9):
            self.solve_cell(x, y)

    def solve_cell(self, x, y):
        if self.grid[x][y] == 0:
            for n in range(9):
                if self.is_possible(y, x, n + 1):
                    print("Value " + str(n + 1) + " possible in (" + str(x) + "," + str(y) + ")")
                    self.grid[x][y] = n + 1
                    self.print()
                    input("Press Enter to continue...")
                    self.solve()
                    self.grid[x][y] = 0
