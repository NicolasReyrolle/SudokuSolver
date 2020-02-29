from math import trunc

class SudokuSolver:
    grid = None

    def load_grid(self, sudoku_grid):
        self.grid = sudoku_grid

    @staticmethod
    def print_frame_line():
        print(("*"+"-"*7)*3+"*")

    def print_grid(self):

        for i in range(9):
            if i % 3 == 0:
                self.print_frame_line()

            line = ""
            for j in range(9):

                if j % 3 == 0:
                    line = line + "| "

                if self.grid[i][j] == 0:
                    value = " "
                else:
                    value = self.grid[i][j]

                line = line + str(value) + " "

            print(line + "|")

        self.print_frame_line()

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
        print(self.is_possible(0, 0, 8))

    def main(self):
        self.load_grid()
        self.solve()
        self.print_grid()


if __name__ == '__main__':
    SudokuSolver.main()
