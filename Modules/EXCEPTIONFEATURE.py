# CHESS PROJECT 2.2

from typing import Type
from Modules import EngineMove, Piece, Pawn

class ExceptionMoves:

    @staticmethod
    def pawnDoubleMove(piece: Type[Piece], engine: Type[EngineMove]) -> None:

        if isinstance(piece, Pawn):
            if piece.name.isupper() and engine.crd[1] == 3 or piece.name.islower() and engine.crd[1] == 4:
                piece.distancing = 1
    
    @staticmethod
    def pawnCaptureMove(piece: Type[Piece], capture: bool) -> None:
        
        if isinstance(piece, Pawn):
            if capture:
                piece.direction = ((1, 1), (-1, 1))
