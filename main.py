from players import Player, Robot
from display import Board

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

        self.player1 = Player(color)
        self.player2 = Robot(self.switchColor[color])
        self.board = Board(self.player1, self.player2)
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
        pass

game = Game(color='white')
print(game.board)
