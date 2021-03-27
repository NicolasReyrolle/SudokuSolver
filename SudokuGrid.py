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

    def is_possible(self, x: int, y: int, n: int) -> bool:
        # Check we do not already have the value
        if self.grid[x][y] != 0:
            return False

        # Check the line
        for j in range(9):
            if self.grid[y][j] == n:
                return False

        # Check the column
        for i in range(9):
            if self.grid[i][x] == n:
                return False

        # Check the square
        square_x = trunc(x / 3)
        square_y = trunc(y / 3)
        for i in range(3):
            for j in range(3):
                if self.grid[square_y * 3 + i][square_x * 3 + j] == n:
                    return False

        # Still there, we are good
        return True

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
