# CHESS PROJECT 2.2

from typing import Type, List
from Fen import Fen


class Board:

    def __init__(self, fen: Type[Fen], rows: int, columns: int) -> None:

        self.fen = fen

        self.rows = rows
        self.columns = columns
        self.blank = '_'
        self.__matrix = [[]]

    @property
    def matrix(self) -> list[list]:
        return self.__matrix

    @matrix.setter
    def matrix(self, new_matrix: List[list]) -> None:
        self.__matrix = new_matrix

    def plot(self) -> None:

        matriz = self.transpose_matrix_to_plot(self.__matrix)

        for sublist in matriz:
            print(sublist)

    @staticmethod
    def transpose_matrix_to_plot(matriz: List[list]) -> List[list]:

        matriz = list(map(list, zip(*matriz)))
        matriz = matriz[::-1]
        return matriz

    @staticmethod
    def transpose_matrix_to_logic(matriz: List[list]) -> List[list]:

        matriz = matriz[::-1]
        matriz = list(map(list, zip(*matriz)))
        return matriz
