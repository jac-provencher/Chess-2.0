import pygame
from players import ChessError, Player, Robot
from display import Board, Window
from position import Position
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
        window = Window(self.player1, self.player2)
        click1 = Position((0, 0))
        click2 = Position((0, 0))
        self.player1.turn = True
        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if not click1.x or not click1.y:
                        click1.x, click1.y = event.pos
                    elif click1.x and click1.y:
                        click2.x, click2.y = event.pos

                        pos1 = click1.convert_inBoardCoordinate()
                        pos2 = click2.convert_inBoardCoordinate()

                        try:
                            if self.player1.turn:
                                opponent = [(piece.pos.x, piece.pos.y) for piece in self.player2.pieces]
                                if pos2 in opponent:
                                    self.player1.eat(self.player2, pos1, pos2, self.gamestate)
                                else:
                                    self.player1.move(pos1, pos2, self.gamestate)

                        except ChessError as error:
                            print(error)
                            print(f"click1 = ({click1.x}, {click1.y})\nclick2 = ({click2.x}, {click2.y})")
                            click1.x, click1.y, click2.x, click2.y = 0, 0, 0, 0

                        else:
                            print(f"click1 = ({click1.x}, {click1.y})\nclick2 = ({click2.x}, {click2.y})")
                            print(self.board)
                            click1.x, click1.y, click2.x, click2.y = 0, 0, 0, 0
                            self.player1.turn = True
                            self.player2.turn = True

            window.redraw()

        pygame.quit()


game = Game(color='white')
print(game.board)
game.mainloop()
