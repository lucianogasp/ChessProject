# CHESS PROJECT 2.2

class Queen:

    def __init__(self, color):
        self.name = 'D'
        self.color = color
        self.direction = ((1, 0), (0, 1), (1, 1), (1, -1))
        self.sense = (1, -1)
        self.distancing = float('inf')
