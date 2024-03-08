# CHESS PROJECT 2.2

class King:

    def __init__(self, color: str):
        self.color = color
        self.name = 'R' if self.color == 'b' else 'r'
        self.direction = ((1, 0), (0, 1), (1, 1), (1, -1))
        self.sense = (1, -1)
        self.distancing = 1

class Queen:

    def __init__(self, color: str):
        self.color = color
        self.name = 'D' if self.color == 'b' else 'd'
        self.direction = ((1, 0), (0, 1), (1, 1), (1, -1))
        self.sense = (1, -1)
        self.distancing = float('inf')

class Rook:

    def __init__(self, color: str):
        self.color = color
        self.name = 'T' if self.color == 'b' else 't'
        self.direction = ((1, 0), (0, 1))
        self.sense = (1, -1)
        self.distancing = float('inf')

class Bishop:

    def __init__(self, color: str):
        self.color = color
        self.name = 'B' if self.color == 'b' else 'b'
        self.direction = ((1, 1), (1, -1))
        self.sense = (1, -1)
        self.distancing = float('inf')

class Knight:

    def __init__(self, color: str):
        self.color = color
        self.name = 'C' if self.color == 'b' else 'c'
        self.direction = ((1, 2), (2, 1), (1, -2), (2, -1))
        self.sense = (1, -1)
        self.distancing = 1

class Pawn:

    def __init__(self, color: str, crd: list, inp: str):
        self.color = color
        self.name = 'P' if self.color == 'b' else 'p'
        self.direction = ((0, 1),)
        self.sense = (-1,) if self.color == 'b' else (1,)
        self.distancing = 1

        if self.color == 'b' and crd[1] == 3 or self.color == 'p' and crd[1] == 4:
            self.distancing += 1
        
        if 'x' in inp:
            self.direction = ((1, 1), (-1, 1))
