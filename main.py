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
fen_values = ['5Q2/8/5Q1Q/8/R6R/8/N7/3N4', 'w', '-', 1]

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

move = Move('TCBDR', board)

inp = move.input_move()
move.input_validation(inp)

'''sliceCrd'''
crd_index = list(re.finditer(r'[a-h][1-8]', inp)).pop().start()
crd0_inpNotation = inp[crd_index]
crd1_inpNotation = inp[crd_index + 1]
'''convertCrds'''
alpha = 'abcdefgh'
crd0 = alpha.index(crd0_inpNotation)
crd1 = int(crd1_inpNotation) - 1
'''settingSelfCrd'''
move.crd = crd0
move.crd = crd1

'''x_Context'''

matrix_value = board.matrix[move.crd[0]][move.crd[1]]
if 'x' in inp:
    if matrix_value == board.blank:
        '''raiseError'''
        raise Exception('"x" not correctly inserted >> must not be used in a move with blank crd')
    elif matrix_value.isupper() and fen.fen['turn'] == 'b':
        '''raiseError'''
        raise Exception(f'illegal move >> {crd0_inpNotation}{crd1_inpNotation} is a square occupied by the white piece "{matrix_value}"')
    elif matrix_value.islower() and fen.fen['turn'] == 'p':
        '''raiseError'''
        raise Exception(f'illegal move >> {crd0_inpNotation}{crd1_inpNotation} is a square occupied by the black piece "{matrix_value}"')
else:
    if matrix_value != board.blank:
        '''raiseError'''
        raise Exception(f'"x" not correctly inserted >> must be used in a move with an occuped crd')

'''crv_Context | crd_Context'''

name = inp[0]

if name.islower():
    pass
elif name == 'D':
    piece = Queen(fen.fen['turn'])

move.find_crv(piece)

move.verify_crv(inp)

move.update_matrix(piece, move.crv)

print(f'crd: {move.crd},\ncrv: {move.crv}\nfen notation: {fen.fen}')
board.plot()