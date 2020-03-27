from pieces import Pawn, Bishop, Queen, King, Knight, Rook

class ChessError(Exception):
    """
    Docstrings
    """

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
        self.turn = False

    def move(self, pos1, pos2, gamestate):
        """
        Docstrings
        """
        for piece in self.pieces:
            currentPosition = (piece.pos.x, piece.pos.y)
            if currentPosition == pos1 and pos2 in piece.moves(gamestate):
                piece.pos.x, piece.pos.y = pos2
                break
        else:
            raise ChessError("Déplacement invalide.")

    def eat(self, opponent, pos1, pos2, board):
        """
        Docstrings
        """
        for piece in self.pieces:
            currentPosition = (piece.pos.x, piece.pos.y)
            if currentPosition == pos1 and pos2 in piece.captures(board):
                piece.pos.x, piece.pos.y = pos2
                opponent.removePiece(pos2)
                break
        else:
            raise ChessError("Aucune pièce n'a pu être éliminée.")

    def promote(self):
        """
        Docstrings
        """
        for i, pawn in enumerate(self.pawns):
            if pawn.pos.y == pawn.endingLine:
                self.pawns[i] = Queen(self.color, (pawn.pos.x, pawn.pos.y))
                return True

        return False

    def removePiece(self, position):
        """
        Docstrings
        """
        for piece in self.pieces:
            if (piece.pos.x, piece.pos.y) == position:
                self.pieces.remove(piece)
                break

    def isCheckmate(self):
        """
        Docstrings
        """
        pass

    def isCheck(self):
        """
        Docstrings
        """
        pass

    def isStalemate(self):
        """
        Docstrings
        """
        pass

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
