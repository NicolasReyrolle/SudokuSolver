
from SudokuGrid import SudokuGrid


class SudokuSolver:
    grid: SudokuGrid = SudokuGrid()

    def load_grid(self, sudoku_grid):
        self.grid.load(sudoku_grid)

    def print_grid(self):
        self.grid.print()

    def main(self):
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

        self.load_grid(grid)
        self.print_grid()
        self.grid.solve()
        self.print_grid()


def print_frame_line():
    print(("*" + "-" * 7) * 3 + "*")


if __name__ == '__main__':
    SudokuSolver().main()
