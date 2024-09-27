# CHESS PROJECT 2.2

from typing import Union
from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def direction(self) -> tuple:
        pass

    @abstractmethod
    def sense(self) -> tuple:
        pass

    @abstractmethod
    def distancing(self) -> Union[int, float]:
        pass
