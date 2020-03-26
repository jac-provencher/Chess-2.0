from players import Player, Robot
from display import Board
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

        return Position().convert(pos1) + Position().convert(pos2)

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

    def mainloop(self):

        self.player1.move((1, 2), (1, 4), self.gamestate)
        self.player1.move((5, 2), (5, 4), self.gamestate)
        print(self.board)
        self.player1.move((1, 1), (1, 3), self.gamestate)
        print(self.board)
        self.player1.move((5, 1), (5, 2), self.gamestate)
        self.player1.move((1, 3), (2, 3), self.gamestate)
        print(self.board)
        self.player1.eat(self.player2, (2, 3), (2, 7), self.gamestate)
        self.player1.move((2, 7), (2, 5), self.gamestate)

game = Game(color='white')
print(game.board)
game.mainloop()
print(game.board)
