import pygame
from itertools import chain

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
            # board[8-y][x-1] = piece.string.upper() if piece.color == 'white' else piece.string.lower()
            board[8-y][x-1] = piece.unicode

        return '\n'.join(' '.join(square for square in row) for row in board) + '\n'

class Window:
    """
    Docstrings
    """
    screenDimension = (696, 696)
    cellDimension = 696//8

    board = pygame.image.load("images/board.png")
    squareContour = pygame.image.load("images/contour.png")
    circle = pygame.image.load("images/circle.png")

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Chess")
        self.screen = pygame.display.set_mode(self.screenDimension)

    def redraw(self, screen, pieces):

        screen.blit(self.board, (0, 0))

        for piece in pieces:
            position = piece.pos.convert_inPixel()
            screen.blit(piece.image, position)

        pygame.display.update()
