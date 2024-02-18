# CHESS PROJECT 2.2

class Queen:

    def __init__(self, color):
        self.color = color
        self.name = 'D' if self.color == 'b' else 'd'
        self.direction = ((1, 0), (0, 1), (1, 1), (1, -1))
        self.sense = (1, -1)
        self.distancing = float('inf')
