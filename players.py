from pieces import Piece
from itertools import product

class Player:
    """
    Docstrings
    """
    def __init__(self, color):

        self.color = color
        self.pieces = [Piece(color, coord, pieceType) for coord, pieceType in
                      zip(product(range(1, 9), range(1, 3)), 'TPCPFPQPKPFPCPTP')]

    def move(self, pos1, pos2):
        """
        Docstrings
        """
        for piece in self.pieces:
            currentPosition = (piece.pos.x, piece.pos.y)
            if currentPosition == pos1 and self.isLegalMove(pos1, pos2):
                piece.pos.x, piece.pos.y = pos2
                break

    def eat(self, opponent, pos1, pos2):
        """
        Docstrings
        """
        self.move(pos1, pos2)
        opponent.removePiece(pos2)

    def isLegalMove(self, pos1, pos2):
        """
        Docstrings
        """
        return True

    def promote(self):
        """
        Docstrings
        """
        pass

    def removePiece(self, position):
        """
        Docstrings
        """
        for i, piece in enumerate(self.pieces):
            if (piece.pos.x, piece.pos.y) == position:
                del self.pieces[i]
                break

class Robot(Player):
    """
    Docstrings
    """
    def __init__(self, color):

        super().__init__(color)
        self.pieces = [Piece(color, coord, pieceType) for coord, pieceType in
                       zip(product(range(1, 9), range(7, 9)), 'ptpcpfpqpkpfpcpt')]

    def minimax(self):
        """
        Docstrings
        """
        pass

    def staticEvaluation(self):
        """
        Docstrings
        """
        pass
