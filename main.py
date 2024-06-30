# CHESS PROJECT 2.2 - EXECUTION

from Modules import Board, Fen, Move, King, Queen, Rook, Bishop, Knight, Pawn

fen = Fen()
board = Board(fen, rows=8, columns=8)

# Default Settings

fen_keys = ['code', 'turn', 'en_passant', 'move']
fen_values = ['rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', 'w', '-', '1']
# fen_values = ['5Q2/3K4/5Q1Q/8/R6R/8/N4BPp/3N4', 'w', '-', 1]

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

move = Move('TCBDR', board)

while True:

    inp = move.input_move()
    move.input_validation(inp)

    crd0_inpNotation, crd1_inpNotation = move.slice_inputCrd(inp)
    move.crd = move.convert_CrdInpNotation(crd0_inpNotation)
    move.crd = move.convert_CrdInpNotation(crd1_inpNotation)

    capture = move.slice_inputCapture(inp)
    move.capture_validation(capture, fen, crd0_inpNotation, crd1_inpNotation)

    name = move.slice_inputName(inp)

    if name.islower():
        piece = Pawn(fen.fen['turn'])
    elif name == 'R':
        piece = King(fen.fen['turn'])
    elif name == 'D':
        piece = Queen(fen.fen['turn'])
    elif name == 'T':
        piece = Rook(fen.fen['turn'])
    elif name == 'B':
        piece = Bishop(fen.fen['turn'])
    elif name == 'C':
        piece = Knight(fen.fen['turn'])
    
    if isinstance(piece, Pawn):
        if capture:
            piece.direction = ((1, 1), (-1, 1))
        if piece.name.isupper() and move.crd[1] == 3 or piece.name.islower() and move.crd[1] == 4:
            piece.distancing = 1

    move.find_crv(piece)
    move.crv_validation(inp)

    # Update Matrix
    move.update_matrix(piece)

    # Update Fen

    matriz = board.transpose_matrix_to_plot(board.matrix)
    fen.fen['code'] = fen.coding(matriz, board.blank)
    fen.fen['turn'] = 'p' if fen.fen['turn'] == 'b' else 'b'
    if fen.fen['turn'] == 'b':
        fen.fen['move'] = str(int(fen.fen['move']) + 1)

    print(f'crd: {move.crd},\ncrv: {move.crv}\nfen notation: {fen.fen}')
    board.plot()

    # Reset Attributes

    move.crd.clear()
    move.crv.clear()
