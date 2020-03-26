from position import Position
from itertools import takewhile, product, chain
from more_itertools import take, tail
import pygame

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
        self.image = pygame.image.load(f"images/pion_{self.color}.png")

    def moves(self, gamestate):
        """
        Docstrings
        """
        move = (self.pos.x, self.pos.y + self.direction)

        return [move, (self.pos.x, self.pos.y + 2*self.direction)] if self.pos.y == self.startingLine else [move]

    def captures(self, gamestate):
        """
        Docstrings
        """
        attacks = []
        for piece in gamestate:
            isOpponent = piece.color == self.switchColor[self.color]
            legalAttack = (piece.pos.x, piece.pos.y) in ((self.pos.x + 1, self.pos.y + 1), (self.pos.x - 1, self.pos.y + 1))
            if isOpponent and legalAttack:
                attacks.append((piece.pos.x, piece.pos.y))

        return attacks

class Rook(Piece):
    string = 'T'
    def __init__(self, color, coord):

        super().__init__(color, coord)
        self.image = pygame.image.load(f"images/tour_{self.color}.png")

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
                    if gamestate.get(position) == self.switchColor[self.color]:
                        attacks.append(position)
                    break
                n += 1

        return attacks

class Knight(Piece):
    string = 'C'
    def __init__(self, color, coord):

        super().__init__(color, coord)
        self.image = pygame.image.load(f"images/cheval_{self.color}.png")

    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for dx, dy in chain(product((-1, 1), (-2, 2)), product((-2, 2), (-1, 1))):
            move = (self.pos.x + dx, self.pos.y + dy)
            if move not in gamestate and self.isOnBoard(move):
                moves.append(move)

        return moves

    def attacks(self, gamestate):
        """
        Docstrings
        """
        opponents = [(piece.pos.x, piece.pos.y) for piece in gamestate if piece.color == self.switchColor[self.color]]
        attacks = []
        for dx, dy in chain(product((-1, 1), (-2, 2)), product((-2, 2), (-1, 1))):
            attack = (self.pos.x + dx, self.pos.y + dy)
            if attack in opponents and self.isOnBoard(attack):
                attacks.append(attack)

        return attacks

class Bishop(Piece):
    string = 'F'
    def __init__(self, color, coord):

        super().__init__(color, coord)
        self.image = pygame.image.load(f"images/fou_{self.color}.png")

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
        gamestate = {(piece.pos.x, piece.pos.y):piece.color for piece in board}
        attacks = []
        for i, j in tail(4, self.pos.vectors):
            n = 1
            while self.isOnBoard(position := (self.pos.x + i*n, self.pos.y + j*n)):
                if position in gamestate:
                    if gamestate[position] == self.switchColor[self.color]:
                        attacks.append(position)
                    break
                n += 1

        return attacks

class Queen(Piece):
    string = 'Q'
    def __init__(self, color, coord):

        super().__init__(color, coord)
        self.image = pygame.image.load(f"images/reine_{self.color}.png")

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
        gamestate = {(piece.pos.x, piece.pos.y):piece.color for piece in board}
        attacks = []
        for i, j in self.pos.vectors:
            n = 1
            while self.isOnBoard(position := (self.pos.x + i*n, self.pos.y + j*n)):
                if position in gamestate:
                    if gamestate.get(position) == self.switchColor[self.color]:
                        attacks.append(position)
                    break
                n += 1

        return attacks

class King(Piece):
    string = 'K'
    def __init__(self, color, coord):

        super().__init__(color, coord)
        self.image = pygame.image.load(f"images/roi_{self.color}.png")

    def moves(self, gamestate):
        """
        Docstrings
        """
        gamestate = [(piece.pos.x, piece.pos.y) for piece in gamestate]
        moves = []
        for i, j in self.pos.vectors:
            move = (self.pos.x + i, self.pos.y + j)
            if move not in gamestate and self.isOnBoard(move):
                moves.append(move)

        return moves

    def attacks(self, gamestate):
        """
        Docstrings
        """
        opponents = [(piece.pos.x, piece.pos.y) for piece in gamestate if piece.color == self.switchColor[self.color]]
        attacks = []
        for i, j in self.pos.vectors:
            attack = (self.pos.x + i, self.pos.y + j)
            if attack in opponents and self.isOnBoard(attack):
                attacks.append(attack)

        return attacks
