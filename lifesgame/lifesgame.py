import os
import time
import copy

FPS = 2
os.system("clear")
greeting = "Welcome to the best game had been created in the fucking life"
print(greeting)
size = int(input("input the numbers of columns and rows you want: "))

FORBBIDEN_NUMBER_MESSAGE1 = """Espera..."""

FORBBIDEN_NUMBER_MESSAGE2 = """dijiste 13?"""

FORBBIDEN_NUMBER_MESSAGE3 = """Aqui tiene pa que me la beses,"""

FORBBIDEN_NUMBER_MESSAGE4 = """Entre mas me la beses mas me crece,"""

FORBBIDEN_NUMBER_MESSAGE5 = """Busca un cura pa que me la rece, y trae un martillo pa que me la endereces,"""

FORBBIDEN_NUMBER_MESSAGE6 = """Por el chiquito se te aparece toas las veces y cuando te estreses aqui te tengo este pa que te desestreses, con este tallo el jopo se te esflorece, se cumple el ciclo hasta que anochece, to los dias y toas las veces, de tanto entablar la raja del jopo se te desaparece, porque este sable no se compadece , si pides napa se te ofrece, y si repites se te agradece, no te hace rico pero tampoco te empobrece, no te hace inteligente pero tampoco te embrutece, y no    paro aqui compa que este nuevamente se endurece. JAJAJAJA
"""

if size == 13:
    print(FORBBIDEN_NUMBER_MESSAGE1)
    time.sleep(1 / 0.5)
    print(FORBBIDEN_NUMBER_MESSAGE2)
    time.sleep(1 / FPS)
    print(FORBBIDEN_NUMBER_MESSAGE3)
    time.sleep(1 / FPS)
    print(FORBBIDEN_NUMBER_MESSAGE4)
    time.sleep(1 / FPS)
    print(FORBBIDEN_NUMBER_MESSAGE5)
    time.sleep(1 / FPS)
    print(FORBBIDEN_NUMBER_MESSAGE6)
    time.sleep(1 / 0.5)
    time.sleep(1 / 0.5)
    input("press enter to continue: ")

print("Choose an initial position: ")
print("A) FAN.")
print("B) AIRCRAFT.")
print("C) AIRCRAFT COLLISION.")
type = input("Write here: ")

print("You typed " + str(size) + ", here your matrix")


board = []
for i in range(size):
    row = []
    for j in range(size):
        row.append('-')
    board.append(row)

if type == ("A") or type == ("a"):
    board[4][5]="*"
    board[5][5]="*"
    board[6][5]="*"
if type == ("B") or type == ("b"):
    board[2][2]="*"
    board[3][3]="*"
    board[3][4]="*"
    board[2][4]="*"
    board[1][4]="*"
if type == ("C") or type == ("c"):
    board[2][2]="*"
    board[3][3]="*"
    board[3][4]="*"
    board[2][4]="*"
    board[1][4]="*"
    board[20][20]="*"
    board[19][19]="*"
    board[19][18]="*"
    board[20][18]="*"
    board[21][18]="*"

def print_board(board):
    os.system("clear")
    for row in board:
        row_str = "  ".join(row)
        print(row_str)


def count_cell_alives(board, row_i, cell_i):
    num_cell_alive = 0
    if cell_i + 1 <= (size - 1) and row_i + 1 <= (size - 1):
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

def check_rules(board):
    new_board = copy.deepcopy(board)
    for row_i, row in enumerate(board):
        for cell_i, cell in enumerate(row):
            check_rule_1(board, new_board, cell, row_i, cell_i)
            check_rule_2(board, new_board, cell, row_i, cell_i)
            check_rule_3(board, new_board, cell, row_i, cell_i)
            check_rule_4(board, new_board, cell, row_i, cell_i)

def check_rule_1(board, new_board, cell, row_i, cell_i):
    num_cell_alive = count_cell_alives(new_board, row_i, cell_i)
    if num_cell_alive < 2 and cell == "*":
        board[row_i][cell_i] = "-"

def check_rule_3(board, new_board, cell, row_i, cell_i):
    num_cell_alive = count_cell_alives(new_board, row_i, cell_i)
    if num_cell_alive > 3 and cell == "*":
        board[row_i][cell_i] = "-"

def check_rule_2(board, new_board, cell, row_i, cell_i):
    num_cell_alive = count_cell_alives(new_board, row_i, cell_i)
    if (num_cell_alive == 2 or num_cell_alive == 3) and cell == "*":
        board[row_i][cell_i] = "*"

def check_rule_4(board, new_board, cell, row_i, cell_i):
    num_cell_alive = count_cell_alives(new_board, row_i, cell_i)
    if num_cell_alive == 3 and cell == "-":
        board[row_i][cell_i] = "*"

while True:
    print_board(board)
    time.sleep(1 / FPS)
    check_rules(board)    # If it is dead and have 3 neighbors, born


