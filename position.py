from display import Window

class Position(Window):
    """
    Docstrings
    """
    def __init__(self, position=(None, None)):

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
        return self.cellDimension*(self.x - 1), self.screenDimension[0] - self.cellDimension*self.y

    def convert_inBoardCoordinate(self):
        """
        Docstrings
        """
        self.x = self.x//self.cellDimension + 1
        self.y = 8 - self.y//self.cellDimension

        return self.x, self.y

def shiftLeft(num, n):
    """
    Returns 'num' with the bits shifted to the right by 'n' places\n
    Example: 11011 << 2 = 1101100
    """
    print(bin(num))
    return bin(num << n)

def shiftRight(num, n):
    """
    Returns 'num' with the bits shifted to the right by 'n' places\n
    Example: 11011 >> 2 = 110
    """
    print(bin(num))
    return bin(num >> n)

def AND(num1, num2):
    """
    Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0\n
    Example: 111011011
             001101001 &
             =========
             001001001
    """
    print(bin(num1))
    print(bin(num2))
    return bin(num1 & num2)

def OR(num1, num2):
    """
    Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.\n
    Example: 1110110011
             1101100010 |
             ==========
             1111110011
    """
    print(bin(num1))
    print(bin(num2))
    return bin(num1 | num2)

def inverse(num):
    """
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1
    """
    print(bin(num))
    return bin(~num)

def exclusiveOR(num1, num2):
    """
    Each bit of the output is the same as the corresponding bit in x if that bit in y is 0,\n
    and it's the complement of the bit in x if that bit in y is 1.
    """
    print(bin(num1))
    print(bin(num2))
    return bin(num1 ^ num2)

"""
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
.  .  .  .  .  .  .  .
.  .  .  .  .  .  .  .
.  .  .  .  .  .  .  .
.  .  .  .  .  .  .  .
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
======================
11111111
11111111
00000000
00000000
00000000
00000000
11111111
11111111
========
0b1111111111111111000000000000000000000000000000001111111111111111

Note:
Créer tous les coups possibles concernant les déplacements
légales et les attaques légales (sous forme de bitboard)

Plusieurs masks devront être coder.
On code des mask à l'aide d'opération semblable à ceux
utilisées sur les ensembles (intersection, union, différence symétrique)
Avec les nombres binaires, on utilise les bitwises operations:
<<
>>
&
|
~
^
"""
