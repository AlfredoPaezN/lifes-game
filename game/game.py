import copy


class Game:

    def __init__(self, board):

        self.__board = board

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, new_board):
        self.__board = new_board

    def __count_cell_alives(self, board, row_i, cell_i):
        num_cell_alive = 0
        if cell_i + 1 <= (self.board.size - 1) and row_i + 1 <= (self.board.size - 1):
            if board[row_i - 1][cell_i - 1] == "*":
                num_cell_alive += 1
            if board[row_i - 1][cell_i] == "*":
                num_cell_alive += 1
            if board[row_i - 1][cell_i + 1] == "*":
                num_cell_alive += 1

            if board[row_i][cell_i + 1] == "*":
                num_cell_alive += 1
            if board[row_i][cell_i - 1] == "*":
                num_cell_alive += 1

            if board[row_i + 1][cell_i - 1] == "*":
                num_cell_alive += 1
            if board[row_i + 1][cell_i] == "*":
                num_cell_alive += 1
            if board[row_i + 1][cell_i + 1] == "*":
                num_cell_alive += 1

        return num_cell_alive

    def __check_rule_1(self, new_board, cell, row_i, cell_i):
        board = self.board.board
        num_cell_alive = self.__count_cell_alives(new_board, row_i, cell_i)
        if num_cell_alive < 2 and cell == "*":
            board[row_i][cell_i] = "-"

    def __check_rule_3(self, new_board, cell, row_i, cell_i):
        board = self.board.board
        num_cell_alive = self.__count_cell_alives(new_board, row_i, cell_i)
        if num_cell_alive > 3 and cell == "*":
            board[row_i][cell_i] = "-"

    def __check_rule_2(self, new_board, cell, row_i, cell_i):
        board = self.board.board
        num_cell_alive = self.__count_cell_alives(new_board, row_i, cell_i)
        if (num_cell_alive == 2 or num_cell_alive == 3) and cell == "*":
            board[row_i][cell_i] = "*"

    def __check_rule_4(self, new_board, cell, row_i, cell_i):
        board = self.board.board
        num_cell_alive = self.__count_cell_alives(new_board, row_i, cell_i)
        if num_cell_alive == 3 and cell == "-":
            board[row_i][cell_i] = "*"

    def check_rules(self):
        board = self.board.board
        new_board = copy.deepcopy(board)
        for row_i, row in enumerate(board):
            for cell_i, cell in enumerate(row):
                self.__check_rule_1(new_board, cell, row_i, cell_i)
                self.__check_rule_2(new_board, cell, row_i, cell_i)
                self.__check_rule_3(new_board, cell, row_i, cell_i)
                self.__check_rule_4(new_board, cell, row_i, cell_i)

