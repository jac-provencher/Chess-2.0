from pieces import Pawn, Bishop, Queen, King, Knight, Rook
from itertools import product, chain
from more_itertools import flatten

class Player:
    """
    Docstrings
    """
    def __init__(self, color, player=1):

        y = 1 if player == 1 else 8
        self.color = color
        self.pawns = [Pawn(color, (x, (2 if player == 1 else 7))) for x in range(1, 9)]
        self.king = King(color, (5, y))
        self.pieces = [Rook(color, (1, y)), Rook(color, (8, y)), Knight(color, (2, y)), Knight(color, (7, y)),
        Bishop(color, (3, y)), Bishop(color, (6, y)), Queen(color, (4, y)), self.king] + self.pawns

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
