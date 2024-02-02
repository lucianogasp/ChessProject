#CHESS PROJECT

from Board import Board
from Fen import Fen
from Piece import Piece

fen = Fen()
board = Board(fen, rows=8, columns=8)

# Chess Start

#board.set_fen(trans=True)
board.set_matrix()
board.plot()