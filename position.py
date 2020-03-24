class Position:
    """
    Docstrings
    """
    def __init__(self, position=(None, None)):

        self.x, self.y = position
        self.conversion = dict(zip(range(1, 9), 'abcdefgh'))

    def convert(self, coord):
        """
        Docstrings
        """
        return self.conversion[coord[0]] + str(coord[1])
