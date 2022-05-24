ROW_SIZE = 3
COLUMN_SIZE = 3


class PositionAlreadyOccupied(Exception):
    """That position is already occupied."""
    pass


class TicTacToe:
    def __init__(self):
        self.player = 0
        self.table_matrix = [["_", "_", "_"], ["_", "_", "_"], [" ", " ", " "]]

    def play(self, row, col):
        if self.table_matrix[row][col] != "_" and self.table_matrix[row][col] != " ":
            raise PositionAlreadyOccupied

        if self.player == 0:
            self.table_matrix[row][col] = "X"
            self.player += 1
        else:
            self.table_matrix[row][col] = "O"
            self.player -= 1

    def won(self):
        for row in range(0, 3):
            if self.table_matrix[row].count("X") == 3:
                return 0
            if self.table_matrix[row].count("O") == 3:
                return 1

        for col in range(0, 3):
            x_counter = 0
            o_counter = 0
            for row in range(0, 3):
                if self.table_matrix[row][col] == "X":
                    x_counter += 1
                    if x_counter == 3:
                        return 0
                elif self.table_matrix[row][col] == "O":
                    o_counter += 1
                    if o_counter == 3:
                        return 1

        if (self.table_matrix[0][0] == "X" and self.table_matrix[1][1] == "X" and self.table_matrix[2][2] == "X") or\
                (self.table_matrix[0][2] == "X" and self.table_matrix[1][1] == "X" and self.table_matrix[2][0] == "X"):
            return 0
        if (self.table_matrix[0][0] == "O" and self.table_matrix[1][1] == "O" and self.table_matrix[2][2] == "O") or\
                (self.table_matrix[0][2] == "O" and self.table_matrix[1][1] == "O" and self.table_matrix[2][0] == "O"):
            return 1
        return -1

    def get_table(self):
        table = ""
        for row in range(0, 3):
            for col in range(0, 3):
                table += f" {self.table_matrix[row][col]} |" if col != 2 else f" {self.table_matrix[row][col]}\n"

        return table


if __name__ == "__main__":
    t = TicTacToe()
    while t.won() == -1:
        pos = input("Insert your position[x y]: ").split()
        t.play(int(pos[0]), int(pos[1]))
        print(t.get_table())

    print("X player won!!!") if t.won() == 0 else print("O player won")
