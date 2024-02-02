class Board:

    def __init__(self, fen: Type[Fen], rows: int, columns: int) -> None:

        self.fen = fen

        self.__rows = rows
        self.__columns = columns
        self.__blank = '_'
        self.__matrix = [[]]

    @property
    def matrix(self) -> list[list]:
        return self.__matrix

    @matrix.setter
    def matrix(self, new_matrix: List[list]) -> None:
        self.__matrix = new_matrix

    def set_fen(self, trans: bool = False) -> None:

        fen_input = self.fen.input()
        self.fen.input_validation(fen_input, self.__rows, self.__columns)
        fen_input = self.fen.dicty(fen_input)

        if trans:
            fen_input = self.fen.translate(fen_input)

        self.fen.fen_attr = fen_input

    def set_matrix(self) -> None:

        self.fen.input_validation(self.fen.fen, self.__rows, self.__columns)
        matriz = self.fen.decoding(blank=self.__blank)
        matriz = self.__transpose_matrix_to_logic(matriz)

        self.matrix = matriz

    def plot(self) -> None:

        matriz = self.__transpose_matrix_to_plot(self.__matrix)

        for sublist in matriz:
            print(sublist)

    @staticmethod
    def __transpose_matrix_to_plot(matriz: List[list]) -> List[list]:

        matriz = list(map(list, zip(*matriz)))
        matriz = matriz[::-1]
        return matriz

    @staticmethod
    def __transpose_matrix_to_logic(matriz: List[list]) -> List[list]:

        matriz = matriz[::-1]
        matriz = list(map(list, zip(*matriz)))
        return matriz

