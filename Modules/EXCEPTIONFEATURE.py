# CHESS PROJECT 2.2

from typing import Type
from Modules import EngineMove, Piece, Pawn, Board, InputMove

class ExceptionMoves:

    @staticmethod
    def pawnDoubleMove(piece: Type[Piece], capture: bool, engine: Type[EngineMove]) -> None:

        if isinstance(piece, Pawn):
            if not capture:
                if piece.name.isupper() and engine.crd[1] == 3 or piece.name.islower() and engine.crd[1] == 4:
                    piece.distancing = 1
    
    @staticmethod
    def pawnCaptureMove(piece: Type[Piece], capture: bool) -> None:
        
        if isinstance(piece, Pawn):
            if capture:
                piece.direction = ((1, 1), (-1, 1))
    
    @staticmethod
    def enpassantMove(piece: Type[Piece], engine: Type[EngineMove], board: Type[Board], move: Type[InputMove]) -> str:
        
        piece_name = piece.name
        engine_crd = engine.crd[1]
        engine_crv = engine.crv[0][1]
        board_matrix_left = board.matrix[engine.crd[0] - 1][engine.crd[1]]
        board_matrix_rigth = board.matrix[engine.crd[0] + 1][engine.crd[1]]

        if all((
            piece_name == 'P',
            engine_crd == 3,
            engine_crv == 1,
            any((
                board_matrix_left == 'p',
                board_matrix_rigth == 'p'
                ))
        )):
            return move.convert_CrMatrix_to_inp(engine.crd[0], engine.crd[1] - 1)
        elif all((
            piece_name == 'p',
            engine_crd == 4,
            engine_crv == 6,
            any((
                board_matrix_left == 'P',
                board_matrix_rigth == 'P'
                ))
        )):
            return move.convert_CrMatrix_to_inp(engine.crd[0], engine.crd[1] + 1)
        else:
            return '-'
