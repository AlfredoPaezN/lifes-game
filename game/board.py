class Board:
    board = []

    def __init__(self, size):
        assert size > 12, "Board's size must be greater than 12"

        self.__size = size
        self.build(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.build(self.size)

    def build(self, size):
        for i in range(size):
            row = []
            for j in range(size):
                row.append('-')
            self.board.append(row)

    def set_initial_position(self, option):
        if option == "A" or option == "a":
            self.board[4][5] = "*"
            self.board[5][5] = "*"
            self.board[6][5] = "*"
        if option == "B" or option == "b":
            self.board[2][2] = "*"
            self.board[3][3] = "*"
            self.board[3][4] = "*"
            self.board[2][4] = "*"
            self.board[1][4] = "*"
        if option == "C" or option == "c":
            self.board[2][2] = "*"
            self.board[3][3] = "*"
            self.board[3][4] = "*"
            self.board[2][4] = "*"
            self.board[1][4] = "*"
            self.board[20][20] = "*"
            self.board[19][19] = "*"
            self.board[19][18] = "*"
            self.board[20][18] = "*"
            self.board[21][18] = "*"

    def show(self):
        _board = """"""
        for row in self.board:
            row_str = "  ".join(row)
            _board += row_str + "\n"
            print(row_str)

        return _board
