# CHESS PROJECT 2.2

from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def direction(self):
        pass

    @abstractmethod
    def sense(self):
        pass

    @abstractmethod
    def distancing(self):
        pass
