from game import *


def test_board():
    board_expected_output = """-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  *  -  -  -  -  -  -  -
-  -  -  -  -  *  -  -  -  -  -  -  -
-  -  -  -  -  *  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
-  -  -  -  -  -  -  -  -  -  -  -  -
"""

    board_test = Board(size=13)
    board_test.set_initial_position("a")

    assert board_test.show() == board_expected_output

