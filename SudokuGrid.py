from math import trunc


class SudokuGrid:
    grid = []

    def __init__(self):

        row = []
        for _ in range(9):
            row.append(0)
            
        for _ in range(9):
            self.grid.append(row) 

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

    def is_possible(self, column: int, line: int, value: int) -> bool:
        """Check if the given value can be set at the given place"""

        # Check we do not already have the value
        if self.grid[column][line] != 0:
            return False

        return (self.is_possible_on_line(line, value) 
                and self.is_possible_on_column(column, value)
                and self.is_possible_on_square(column, line, value)
        )

    def is_possible_on_line(self, line: int, value: int) -> bool:
        """Check if a value is possible on the line"""

        is_possible = True

        for j in range(9):
            if self.grid[line][j] == value:
                is_possible = False
                break

        return is_possible

    def is_possible_on_column(self, column: int, value: int) -> bool:
        """Check if a value is possible on the column"""

        is_possible = True

        for i in range(9):
            if self.grid[i][column] == value:
                is_possible = False
                break

        return is_possible

    def is_possible_on_square(self, column: int, line: int, value: int) -> bool:
        """Check if a value is possible on its square"""

        is_possible = True

        square_column = trunc(column / 3)
        square_line = trunc(line / 3)
        for i in range(3):
            for j in range(3):
                if self.grid[square_line * 3 + i][square_column * 3 + j] == value:
                    is_possible = False
                    break
                
        return is_possible

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
