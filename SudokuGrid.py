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
