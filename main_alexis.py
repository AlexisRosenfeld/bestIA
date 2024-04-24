from interfaces import Board, Token
from Rosenfeld_Simonet import GroupeDavidStrategy as Stra
import copy

r = Token.RED
y = Token.YELLOW
e = Token.EMPTY

# Create a new board instance
m_b = Board(6, 7, 4)
m_b.play(0, r)
m_b.play(2, y)
m_b.play(2, r)
Stra().play(m_b, r)
