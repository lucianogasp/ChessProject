# CHESS PROJECT 2.2

from typing import List, Union


class Fen:

    def __init__(self):

        self._fen = None

    @property
    def fen(self) -> dict:
        return self._fen

    @fen.setter
    def fen(self, new_fen: dict) -> None:
        self._fen = new_fen
    def decoding(self, blank: str) -> List[list]:

        fen_split = self._fen['code'].split('/')
        matriz = list()

        for row in fen_split:
            sublist = list()
            for square in row:
                if square.isdigit():
                    sublist += [blank] * int(square)
                else:
                    sublist += square
            matriz.append(sublist)

        return matriz

    @staticmethod
    def set_fen(fen_keys: list, fen_values: list) -> dict:

        if len(fen_keys) != len(fen_values):
            raise IndexError('wrong input on KEY-VALUE LISTS >> they must be the same length')

        fen_dict = dict()
        for key, value in zip(fen_keys, fen_values):
            fen_dict[key] = value
        
        return fen_dict

    @staticmethod
    def translate(fen: dict, keys: list, trans_list: list) -> dict:

        if len(trans_list) % 2 != 0:
            raise IndexError('wrong input on TRANSLATION LISTS >> every source must have its own translation')
        
        source = trans_list[::2]
        translated = trans_list[1::2]
        for k, src, trans in zip(keys, source, translated):
            fen[k] = fen[k].translate(str.maketrans(str(src), str(trans)))
        
        return fen

    @staticmethod
    def fen_validation(fen_input: dict, n_rows: int, n_columns: int) -> None:

        fen_notation = list(fen_input.values())
        fen_code = fen_notation[0].split('/')

        if len(fen_notation) != 4:
            raise ValueError(f'wrong input on FEN NOTATION >> fen must contain 4 elements. '
                             f'It has {len(fen_notation)} instead...')
        if len(fen_code) != n_rows:
            raise ValueError(f'wrong input on FEN NOTATION >> fen code must contain {n_rows} rows. '
                             f'It has {len(fen_code)} instead...')
        for i, line in enumerate(fen_code):
            cont = 0
            for square in line:
                if square.isdigit():
                    cont += int(square)
                else:
                    cont += 1
            if cont != n_columns:
                raise ValueError(
                    f'wrong input on FEN NOTATION >> fen code must contain '
                    f'{n_columns} columns instead of {cont} at the row {len(fen_code) - i}')
