
from SudokuGrid import SudokuGrid


class SudokuSolver:
    grid: SudokuGrid = SudokuGrid()

    def load_grid(self, sudoku_grid):
        self.grid.load(sudoku_grid)

    def print_grid(self):
        self.grid.print()

    def main(self):
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

        self.load_grid(grid)
        self.print_grid()
        self.grid.solve()
        self.print_grid()


def print_frame_line():
    print(("*" + "-" * 7) * 3 + "*")


if __name__ == '__main__':
    SudokuSolver().main()
