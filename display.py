from itertools import chain

class Window:
    """
    Docstrings
    """
    def __init__(self):
        pass

class Board:
    """
    Docstrings
    """
    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

    def __str__(self):

        board = [['.' for x in range(8)] for y in range(8)]
        for piece in chain(self.player1.pieces, self.player2.pieces):
            x, y = piece.pos.x, piece.pos.y
            board[8-y][x-1] = piece.pieceType

        return '\n'.join(' '.join(square for square in row) for row in board) + '\n'

    def pygameDisplay(self):
        screen = Window()
