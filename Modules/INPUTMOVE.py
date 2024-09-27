# CHESS PROJECT 2.2

from typing import Type, Tuple
from Modules import Board
import re

class InputMove:

    def __init__(self, piece_names) -> None:

        self.__regex_generic = rf'^(?:[{piece_names}][a-h]?[1-8]?x?|[a-h]x)?[a-h][1-8](?:=[A-Z])?(?:\+|\+\+|#)?$'
    
    def input_move(self) -> str:
        return input('Digite seu lance: ').strip()

    def input_validation(self, inp: str, regexp: str=None) -> None:

        if regexp is None:
            regexp = self.__regex_generic

        verify = re.search(regexp, inp)
        if not verify:
            '''raise Error'''
            raise re.error(f'"{regexp}" pattern did not match in the input string "{inp}"')
    
    @staticmethod
    def slice_inputCrd(inp: str) -> Tuple[str, str]:

        crd_index = list(re.finditer(r'[a-h][1-8]', inp)).pop().start()
        crd0_inpNotation = inp[crd_index]
        crd1_inpNotation = inp[crd_index + 1]
        return crd0_inpNotation, crd1_inpNotation

    @staticmethod
    def convert_CrInp_to_matrix(input: str) -> Tuple[int, int]:
        
        if input.isalpha():
            cr0 = ord(input) - ord('a')
            return cr0
        elif input.isdigit():
            cr1 = int(input) - 1
            return cr1
        elif input.isalnum():
            cr0 = ord(input[0]) - ord('a')
            cr1 = int(input[1]) - 1
            return cr0, cr1
    
    @staticmethod
    def convert_CrMatrix_to_inp(cr0: int, cr1: int) -> str:
        
        crAlpha = chr(cr0 + ord('a'))
        crNum = str(cr1 + 1)
        return crAlpha + crNum


    @staticmethod
    def slice_inputCapture(inp: str) -> bool:

        if 'x' in inp:
            capture = True
        else:
            capture = False
        return capture

    def capture_validation(self, board: Type[Board], capture: bool, turn: str, crd0: int, crd1: int, crd0_inpNotation: str, crd1_inpNotation: str) -> None:
        
        matrix_value = board.matrix[crd0][crd1]

        if capture:
            if matrix_value == board.blank:
                '''raiseError'''
                raise Exception('"x" not correctly inserted >> must not be used in a move with blank crd')
            if matrix_value.isupper() and turn == 'b':
                '''raiseError'''
                raise Exception(f'illegal move >> {crd0_inpNotation}{crd1_inpNotation} is a square occupied by the white piece "{matrix_value}"')
            if matrix_value.islower() and turn == 'p':
                '''raiseError'''
                raise Exception(f'illegal move >> {crd0_inpNotation}{crd1_inpNotation} is a square occupied by the black piece "{matrix_value}"')
        else:
            if matrix_value != board.blank:
                '''raiseError'''
                raise Exception(f'"x" not correctly inserted >> must be used in a move with an occupied crd')

    @staticmethod
    def slice_inputName(inp: str) -> str:

        name = inp[0]
        return name
    
    @staticmethod
    def slice_inputCrv(inp: str) -> str:

        crv_reObject = list(re.finditer(r'[a-h][1-8]|[a-h]|[1-8]', inp))
        crv_reObject.pop()
        if not crv_reObject:
            return None
        crv_reObject, = crv_reObject
        crv_index_start = crv_reObject.start()
        crv_index_end = crv_reObject.end()
        crv_inpNotation = inp[crv_index_start:crv_index_end]
        return crv_inpNotation
