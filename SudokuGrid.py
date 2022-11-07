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

    def set_value_at(self, line: int, column: int, value: int):
        self.grid[line][column] = value

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
    def get_first_possible_value(self, line: int, column: int) -> int:
        if self.get_value_at(line, column) != 0:
            return self.get_value_at(line, column)
        else:
            for n in range(1, 10):
                if self.is_possible(line, column, n):
                    return n

        # If we are here it means there is no possible value
        raise Exception("No possible value found")

    # Count the number of possible values in one box
    def count_possible_values(self, line: int, column: int) -> int:
        count = 0
        for n in range(1, 10):
            if self.is_possible(line, column, n):
                count = count + 1
        return count

    # Solve (by rows) the boxes where there is only one possibility and return the number of boxes solved
    def solve_single_possibility(self) -> int:
        count = 0

        for line in range(9):
            for column in range(9):
                if self.count_possible_values(line, column) == 1:
                    self.set_value_at(line, column, self.get_first_possible_value(line, column))
                    count = count + 1

        return count

    def solve(self):

        stage = 1

        while True:
            self.print()

            number_resolved = 0
            number_resolved = number_resolved + self.solve_single_possibility()

            print("Stage " + str(stage) + " - " + str(number_resolved) + " box(es) resolved")

            if number_resolved == 0:
                break

            stage = stage + 1
