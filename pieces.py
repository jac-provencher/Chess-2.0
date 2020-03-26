from position import Position
from itertools import takewhile, product, chain
from more_itertools import take, tail

class Piece:
    """
    Docstrings
    """
    switchColor = {'white' : 'black', 'black' : 'white'}

    def __init__(self, color, coord):
        self.color = color
        self.pos = Position(coord)

    def isOnBoard(self, position):
        """
        Docstrings
        """
        x, y = position
        return 1 <= x <= 8 and 1 <= y <= 8

class Pawn(Piece):
    string = 'P'
    def __init__(self, color, coord):
        super().__init__(color, coord)
        self.startingLine = coord[1]
        self.direction = 1 if coord[1] == 2 else -1
        self.move = (self.pos.x, self.pos.y + self.direction)

    def moves(self, gamestate):
        """
        Docstrings
        """
        return [self.move, (self.pos.x, self.pos.y + 2*self.direction)] if self.pos.y == self.startingLine else list(self.move)

    def attacks(self, gamestate):
        """
        Docstrings
        """
        pass

class Rook(Piece):
    string = 'T'
    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for i, j in take(4, self.pos.vectors):
            direction = []
            n = 1
            while self.isOnBoard(move := (self.pos.x + i*n, self.pos.y + j*n)) and (self.pos.x + i*n, self.pos.y + j*n) not in gamestate:
                direction.append(move)
                n += 1
            moves += direction

        return moves

    def captures(self, board):
        """
        Docstrings
        """
        gamestate = {(piece.pos.x, piece.pos.y):piece.color for piece in board}
        attacks = []
        for i, j in take(4, self.pos.vectors):
            n = 1
            while self.isOnBoard(position := (self.pos.x + i*n, self.pos.y + j*n)):
                if position in gamestate:
                    if gamestate[position] == self.switchColor[self.color]:
                        attacks.append(position)
                    break
                n += 1

        return attacks

class Knight(Piece):
    string = 'C'
    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for dx, dy in chain(product((-1, 1), (-2, 2)), product((-2, 2), (-1, 1))):
            if (self.pos.x+dx, self.pos.y+dy) not in gamestate and self.isOnBoard(move := (self.pos.x+dx, self.pos.y+dy)):
                moves.append(move)

        return moves

    def attacks(self, gamestate):
        """
        Docstrings
        """
        pass

class Bishop(Piece):
    string = 'F'
    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for i, j in tail(4, self.pos.vectors):
            direction = []
            n = 1
            while self.isOnBoard(move := (self.pos.x + i*n, self.pos.y + j*n)) and (self.pos.x + i*n, self.pos.y + j*n) not in gamestate:
                direction.append(move)
                n += 1
            moves += direction

        return moves

    def attacks(self, gamestate):
        """
        Docstrings
        """
        pass

class Queen(Piece):
    string = 'Q'
    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for i, j in self.pos.vectors:
            direction = []
            n = 1
            while self.isOnBoard(move := (self.pos.x + i*n, self.pos.y + j*n)) and (self.pos.x + i*n, self.pos.y + j*n) not in gamestate:
                direction.append(move)
                n += 1
            moves += direction

        return moves

    def attacks(self, gamestate):
        """
        Docstrings
        """
        pass

class King(Piece):
    string = 'K'
    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for i, j in self.pos.vectors:
            if (self.pos.x+i, self.pos.y+j) not in gamestate and self.isOnBoard(move := (self.pos.x+i, self.pos.y+j)):
                moves.append(move)

        return moves

    def attacks(self, gamestate):
        """
        Docstrings
        """
        pass
