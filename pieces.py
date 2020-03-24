from position import Position
from itertools import chain, takewhile
from more_itertools import take, tail, first_true

class Piece:
    """
    Docstrings
    """
    def __init__(self, color, coord):
        self.color = color
        self.pos = Position(coord)

class Pawn(Piece):
    string = 'P'
    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Rook(Piece):
    string = 'T'
    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Knight(Piece):
    string = 'C'
    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Bishop(Piece):
    string = 'F'
    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Queen(Piece):
    string = 'Q'
    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class King(Piece):
    string = 'K'
    def validMoves(self, board):
        """
        Docstrings
        """
        pass
