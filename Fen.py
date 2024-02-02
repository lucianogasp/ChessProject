class Fen:

    def __init__(self):
        self.fen = {
            'code': 'tcbdrbct/pppppppp/8/8/8/8/PPPPPPPP/TCBDRBCT',
            'turn': 'b',
            'en_passant': '-',
            'move': 1
        }

    @property
    def fen_attr(self) -> dict:
        return self.fen

    @fen_attr.setter
    def fen_attr(self, new_fen: dict) -> None:
        self.fen = new_fen

    def input(self) -> str:

        fen_input = input('Digite o valor fen: ').strip()
        return fen_input

    def decoding(self, blank: str) -> List[list]:

        fen_split = self.fen['code'].split('/')
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
    def dicty(fen: str) -> dict:

        fen_split = fen.split()
        fen_dict = dict()
        fen_dict['code'] = fen_split[0]
        fen_dict['turn'] = fen_split[1]
        fen_dict['en_passant'] = fen_split[2]
        fen_dict['move'] = fen_split[3]
        return fen_dict

    @staticmethod
    def translate(fen: dict) -> dict:

        fen['code'] = fen['code'].translate(str.maketrans('rnqkRNQK', 'tcdrTCDR'))
        fen['turn'] = fen['turn'].translate(str.maketrans('wb', 'bp'))
        return fen

    @staticmethod
    def input_validation(fen_input: Union[str, dict], n_rows: int, n_columns: int) -> None:

        if isinstance(fen_input, dict):
            fen_input = ' '.join(map(str, fen_input.values()))

        fen_notation = fen_input.split()
        fen_code = fen_notation[0].split('/')

        if len(fen_notation) != 4:
            raise ValueError(f'wrong input on fen notation >> fen must contain 4 elements. '
                             f'It has {len(fen_notation)} instead...')
        if len(fen_code) != n_rows:
            raise ValueError(f'wrong input on fen notation >> fen code must contain {n_rows} rows. '
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
                    f'wrong input on fen notation >> fen code must contain '
                    f'{n_columns} columns instead of {cont} at the row {len(fen_code) - i}')

