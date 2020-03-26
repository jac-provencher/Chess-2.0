class Position:
    """
    Docstrings
    """
    def __init__(self, position):

        self.x, self.y = position
        self.vectors = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        self.conversion = dict(zip(range(1, 9), 'abcdefgh'))

    def convert(self, coord):
        """
        Docstrings
        """
        return self.conversion[coord[0]] + str(coord[1])
