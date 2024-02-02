# CHESS PROJECT 2.2 - EXECUTION

from Board import Board
from Fen import Fen
from Move import Move
from Piece import Queen

fen = Fen()
move = Move()
board = Board(fen, rows=8, columns=8)

# Default Settings

fen_keys = ['code', 'turn', 'en_passant', 'move']
fen_values = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', 'w', '-', 1]

trans = True
trans_keys = ['code', 'turn']
trans_list = ['rnqkRNQK', 'tcdrTCDR', 'wb', 'bp']

# FEN Settings

fen_input = fen.set_fen(fen_keys, fen_values)
fen.fen_validation(fen_input, n_rows=board.rows, n_columns=board.columns)
if trans:
    fen_input = fen.translate(fen_input, keys=trans_keys, trans_list=trans_list)
fen.fen = fen_input

# Matrix Settings

matriz = fen.decoding(blank=board.blank)
matriz = board.transpose_matrix_to_logic(matriz)
board.matrix = matriz

# Plot Matrix
board.plot()

# Move

inp = move.input_move()
'''move.input_validation(inp)'''

name = inp[0]

alpha = 'abcdefgh'
coord1 = alpha.index(inp[-2])
coord2 = int(inp[-1]) - 1
move.crd = inp[coord1, coord2]

if name.islower():
    pass
elif name == 'D':
    piece = Queen(fen.fen['turn'])

move.find_crv()