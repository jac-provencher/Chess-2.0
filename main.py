import pygame
from players import Player, Robot
from display import Board, Window
from itertools import chain


class History:
    """
    Docstrings
    """
    records = {}

    def __init__(self):

        self.record = []

    def addMove(self, move):
        """
        Docstrings
        """
        self.record.append(self.uci(move))

    def clearAll(self):
        """
        Docstrings
        """
        self.records.clear()

    def uci(self, move):
        """
        Docstrings
        """
        pos1, pos2 = move

        return Position().convert_inString(pos1) + Position().convert_inString(pos2)

class Game:
    """
    Docstrings
    """
    switchColor = {'white' : 'black', 'black' : 'white'}

    def __init__(self, color='white'):

        self.player1 = Player(color, player=1)
        self.player2 = Robot(self.switchColor[color], player=2)
        self.board = Board(self.player1, self.player2)
        self.gamestate = list(chain(self.player1.pieces, self.player2.pieces))
        self.history = History()

    def mainloop(self):
        """
        Docstrings
        """
        window = Window()
        running = True
        self.player1.turnToPlay = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            window.redraw(window.screen, self.gamestate)

        pygame.quit()


game = Game(color='white')
print(game.board)
game.mainloop()
