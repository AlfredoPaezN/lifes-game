import os
import time

from game import *


FPS = 2
os.system("clear")

# Asks the size of the board
size = int(input("input the numbers of columns and rows you want: "))

# Forbidden Number Messages
if size == 13:
    messages = [MESSAGE_ONE, MESSAGE_TWO, MESSAGE_THREE, MESSAGE_FIVE, MESSAGE_SIX]
    for message in messages:
        message.show()
        time.sleep(1 / FPS)
    input("press enter to continue: ")


# Options Messages
messages = [MESSAGE_SEVEN, MESSAGE_EIGHT, MESSAGE_NINE, MESSAGE_TEN]
for message in messages:
    message.show()

# Select an initial position
option = input("Write here: ")

# Initialize all the classes to prepare the game
board = Board(size)
board.set_initial_position(option)
game = Game(board)

if __name__ == '__main__':
    # Running the game
    while True:
        board.show()
        time.sleep(1 / FPS)
        game.check_rules()
        Screen.clear()
