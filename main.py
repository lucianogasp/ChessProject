# CHESS PROJECT 2.2 - EXECUTION

from Board import Board
from Fen import Fen
from Move import Move
from Piece import Queen

import re

fen = Fen()
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

'''name_Context'''

move = Move('TCBDR')

inp = move.input_move()
move.input_validation(inp)

'''sliceCrd'''
crd_index = list(re.finditer(r'[a-h][1-8]', inp)).pop().start()
crd0 = inp[crd_index]
crd1 = inp[crd_index + 1]
'''convertCrds'''
alpha = 'abcdefgh'
crd0 = alpha.index(crd0)
crd1 = int(crd1) - 1
'''settingSelfCrd'''
move.crd = crd0
move.crd = crd1

'''x_Context'''

matrix_value = board.matrix[move.crd[0]][move.crd[1]]
if 'x' in inp:
    if matrix_value == board.blank:
        '''raiseError'''
    elif matrix_value.isupper() and fen.fen['turn'] == 'b':
        '''raiseError'''
    elif matrix_value.islower() and fen.fen['turn'] == 'p':
        '''raiseError'''
else:
    if matrix_value != board.blank:
        '''raiseError'''

'''crv_Context | crd_Context'''

name = inp[0]

if name.islower():
    pass
elif name == 'D':
    piece = Queen(fen.fen['turn'])

move.find_crv()

'''move.verify_crv(inp)'''
