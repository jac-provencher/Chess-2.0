from position import Position

class Piece:
    """
    Docstrings
    """
    def __init__(self, color, coord, pieceType):
        self.color = color
        self.pos = Position(coord)
        self.pieceType = pieceType

class Pawn:

    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Tour:

    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Cheval:

    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Fou:

    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class Queen:

    def validMoves(self, board):
        """
        Docstrings
        """
        pass

class King:

    def validMoves(self, board):
        """
        Docstrings
        """
        pass
