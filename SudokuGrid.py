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

    def is_possible(self, line: int, column: int, value: int) -> bool:
        """Check if the given value can be set at the given place"""

        # Check we do not already have the value
        if self.get_value_at(line, column) != 0:
            return False

        return (self.is_possible_on_line(line, value)
                and self.is_possible_on_column(column, value)
                and self.is_possible_on_square(line, column, value)
        )

    def is_possible_on_line(self, line: int, value: int) -> bool:
        """Check if a value is possible on the line"""

        is_possible = True

        for j in range(9):
            if self.get_value_at(line, j) == value:
                is_possible = False
                break

        return is_possible

    def is_possible_on_column(self, column: int, value: int) -> bool:
        """Check if a value is possible on the column"""

        is_possible = True

        for i in range(9):
            if self.get_value_at(i, column) == value:
                is_possible = False
                break

        return is_possible

    def is_possible_on_square(self, line: int, column: int, value: int) -> bool:
        """Check if a value is possible on its square"""

        is_possible = True

        square_column = trunc(column / 3)
        square_line = trunc(line / 3)
        for i in range(3):
            for j in range(3):
                if self.get_value_at(square_line * 3 + i, square_column * 3 + j) == value:
                    is_possible = False
                    break
            if not is_possible:
                break

        return is_possible

    def solve(self):
        """Try to resolve the puzzle"""
        while(True):
            values_found = False
            for x in range(9):
                if self.solve_row(x):
                    values_found = True
            if not values_found:
                # We cannot go further on the resolution
                break

    def solve_row(self, x):
        """Try to solve a line, return true if at least one value found"""
        count_found = 0
        for y in range(9):
            if self.solve_cell(x, y):
                count_found += 1
                
        return count_found > 0

    def solve_cell(self, line: int, column: int) -> bool:
        """Try to find the value at a specific cell, return true if solution found"""

        count_possible_at_cell = 0
        if self.get_value_at(line, column) == 0:
            possible_value = 0
            for n in range(9):
                if self.is_possible(line, column, n + 1):
                    possible_value = n + 1
                    count_possible_at_cell += 1

            if count_possible_at_cell == 1:
                print("Value " + str(possible_value) + 
                      " found in (" + str(line) + "," + str(column) + ")")
                self.set_value_at(line, column, possible_value)
    
        return count_possible_at_cell == 1

    def get_value_at(self, line: int, column: int) -> int:
        """Return the current value at the given position"""
        return self.grid[line][column]

    def set_value_at(self, line: int, column: int, value: int):
        """Set the value at the given position"""
        self.grid[line][column] = value
