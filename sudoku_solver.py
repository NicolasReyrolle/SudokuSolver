"""Sudoku solver main module."""
from sudoku_grid import SudokuGrid


class SudokuSolver:
    """Sudoku solver class."""

    def __init__(self):
        self.grid = SudokuGrid()

    def load_grid(self, sudoku_grid: list[list[int]]) -> None:
        """Load a sudoku grid."""
        self.grid.load(sudoku_grid)

    def print_grid(self) -> None:
        """Print the sudoku grid."""
        self.grid.print()

    def main(self) -> None:
        """Main entry point."""
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


if __name__ == '__main__':
    SudokuSolver().main()
