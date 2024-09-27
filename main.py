# CHESS PROJECT 2.2 - EXECUTION

from Modules import Fen, Board, InputMove, EngineMove, King, Queen, Rook, Bishop, Knight, Pawn, ExceptionMoves

fen = Fen()
board = Board(fen, rows=8, columns=8)

# Default Settings

fen_keys = ['code', 'turn', 'en_passant', 'move']
fen_values = ['rnbqkbnr/ppp1pppp/8/3pP3/8/8/PPPP1PPP/RNBQKBNR', 'b', '-', '1']
# fen_values = ['1R3Q2/3K4/5Q1Q/4p3/R2PPp1R/2p5/N2P2P1/1R1N4', 'w', '-', 1]

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

move = InputMove('TCBDR')
engine = EngineMove(board)

while True:

    # Input / Validation

    inp = move.input_move()
    move.input_validation(inp)

    # Slicing Piece Name / Instantiating

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
    
    # Slicing Crd Input / Setting Crd

    crd0_inpNotation, crd1_inpNotation = move.slice_inputCrd(inp)
    engine.crd = move.convert_CrInp_to_matrix(crd0_inpNotation)
    engine.crd = move.convert_CrInp_to_matrix(crd1_inpNotation)

    # Slicing Capture Input / Validation

    capture = move.slice_inputCapture(inp)
    try:
        move.capture_validation(board, capture, fen.fen['turn'], engine.crd[0], engine.crd[1], crd0_inpNotation, crd1_inpNotation)
    except Exception as exception:
        inpCrd = crd0_inpNotation + crd1_inpNotation
        if piece.name in 'Pp' and inpCrd == fen.fen['en_passant']:
            pass
        else:
            raise exception

    # Exception Moves

    ExceptionMoves().pawnDoubleMove(piece, capture, engine)
    ExceptionMoves().pawnCaptureMove(piece, capture)

    # Move / Validation

    engine.find_crv(piece)
    engine.crv_validation(inp, move)

    # Update Matrix
    engine.update_matrix(engine.crd[0], engine.crd[1], piece.name)
    engine.update_matrix(engine.crv[0][0], engine.crv[0][1], board.blank)

    inpCrd = crd0_inpNotation + crd1_inpNotation
    if piece.name == 'P' and inpCrd == fen.fen['en_passant']:
        engine.update_matrix(engine.crd[0], engine.crd[1] - 1, board.blank)
    if piece.name == 'p' and inpCrd == fen.fen['en_passant']:
        engine.update_matrix(engine.crd[0], engine.crd[1] + 1, board.blank)    

    # Update Fen

    matriz = board.transpose_matrix_to_plot(board.matrix)
    fen.fen['code'] = fen.coding(matriz, board.blank)
    fen.fen['turn'] = 'p' if fen.fen['turn'] == 'b' else 'b'

    fen.fen['en_passant'] = ExceptionMoves().enpassantMove(piece, engine, board, move)

    if fen.fen['turn'] == 'b':
        fen.fen['move'] = str(int(fen.fen['move']) + 1)

    print(f'crd: {engine.crd},\ncrv: {engine.crv}\nfen notation: {fen.fen}')
    board.plot()

    # Reset Attributes

    del engine.crd
    del engine.crv
