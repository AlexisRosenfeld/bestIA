from interfaces import Board, Token
from Rosenfeld_Simonet import GroupeDavidStrategy as Stra
import copy

r = Token.RED
y = Token.YELLOW
e = Token.EMPTY

# Create a new board instance
mb = Board(6, 7, 4)
