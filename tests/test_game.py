from game import Game, Board


def test_game():
    board = Board(size=13)
    game = Game(board)

    assert game.board == board



