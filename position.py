class Position:
    """
    Docstrings
    """
    def __init__(self, position):

        self.x, self.y = position
        self.vectors = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        self.conversion = dict(zip(range(1, 9), 'abcdefgh'))

    def convert_inString(self, coord):
        """
        Docstrings
        """
        return self.conversion[coord[0]] + str(coord[1])

    def convert_inPixel(self):
        """
        Docstrings
        """
        return 87*(self.x - 1), 696 - 87*self.y

    def convert_inBoardCoordinate(self):
        """
        Docstrings
        """
        self.x = self.x//87 + 1
        self.y = 8 - self.y//87

        return self.x, self.y
