# CHESS PROJECT 2.2

from Modules import Piece

class King (Piece):

    def __init__(self, color: str) -> None:

        self._name = 'R' if color == 'b' else 'r'
        self._direction = ((1, 0), (0, 1), (1, 1), (1, -1))
        self._sense = (1, -1)
        self._distancing = 1

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def direction(self) -> tuple:
        return self._direction
    
    @property
    def sense(self) -> tuple:
        return self._sense
    
    @property
    def distancing(self) -> int:
        return self._distancing


class Queen (Piece):

    def __init__(self, color: str) -> None:

        self._name = 'D' if color == 'b' else 'd'
        self._direction = ((1, 0), (0, 1), (1, 1), (1, -1))
        self._sense = (1, -1)
        self._distancing = float('inf')

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def direction(self) -> tuple:
        return self._direction
    
    @property
    def sense(self) -> tuple:
        return self._sense
    
    @property
    def distancing(self) -> float:
        return self._distancing


class Rook (Piece):

    def __init__(self, color: str) -> None:

        self._name = 'T' if color == 'b' else 't'
        self._direction = ((1, 0), (0, 1))
        self._sense = (1, -1)
        self._distancing = float('inf')

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def direction(self) -> tuple:
        return self._direction
    
    @property
    def sense(self) -> tuple:
        return self._sense
    
    @property
    def distancing(self) -> float:
        return self._distancing


class Bishop (Piece):

    def __init__(self, color: str) -> None:

        self._name = 'B' if color == 'b' else 'b'
        self._direction = ((1, 1), (1, -1))
        self._sense = (1, -1)
        self._distancing = float('inf')

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def direction(self) -> tuple:
        return self._direction
    
    @property
    def sense(self) -> tuple:
        return self._sense
    
    @property
    def distancing(self) -> float:
        return self._distancing


class Knight (Piece):

    def __init__(self, color: str) -> None:

        self._name = 'C' if color == 'b' else 'c'
        self._direction = ((1, 2), (2, 1), (1, -2), (2, -1))
        self._sense = (1, -1)
        self._distancing = 1

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def direction(self) -> tuple:
        return self._direction
    
    @property
    def sense(self) -> tuple:
        return self._sense
    
    @property
    def distancing(self) -> int:
        return self._distancing


class Pawn (Piece):

    def __init__(self, color: str) -> None:
        
        self._name = 'P' if color == 'b' else 'p'
        self._direction = ((0, 1),)
        self._sense = (-1,) if color == 'b' else (1,)
        self._distancing = 1
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def direction(self) -> tuple:
        return self._direction
    
    @property
    def sense(self) -> tuple:
        return self._sense
    
    @property
    def distancing(self) -> int:
        return self._distancing

    @direction.setter
    def direction(self, new_direction) -> None:
        self._direction = new_direction

    @distancing.setter
    def distancing(self, increment) -> None:
        self._distancing += increment
