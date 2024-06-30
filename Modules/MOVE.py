# CHESS PROJECT 2.2

from typing import Type
from Modules import Fen, Piece

import re

class Move:

    def __init__(self, piece_names: str, board: Type[any]) -> None:

        self._crd = list()
        self._crv = list()
        self.__regex_generic = rf'^(?:[{piece_names}][a-h]?[1-8]?x?|[a-h]x)?[a-h][1-8](?:=[A-Z])?(?:\+|\+\+|#)?$'
        
        self.board = board
        
    @property
    def crd(self) -> list:
        return self._crd
    
    @crd.setter
    def crd(self, value: int) -> None:
        self._crd.append(value)
    
    @property
    def crv(self) -> list:
        return self._crv
    
    @crv.setter
    def crv(self, value: tuple) -> None:
        self.crv.append(value)

    def input_move(self) -> str:
        return input('Digite seu lance: ').strip()

    def input_validation(self, inp: str, regexp: str=None) -> None:

        if regexp is None:
            regexp = self.__regex_generic

        verify = re.search(regexp, inp)
        if not verify:
            '''raise Error'''
            raise re.error(f'"{regexp}" pattern did not match in the input string "{inp}"')

    def capture_validation(self, capture: bool, fen: Type[Fen], crd0_inpNotation: str, crd1_inpNotation: str) -> None:
        
        matrix_value = self.board.matrix[self.crd[0]][self.crd[1]]

        if capture:
            if matrix_value == self.board.blank:
                '''raiseError'''
                raise Exception('"x" not correctly inserted >> must not be used in a move with blank crd')
            elif matrix_value.isupper() and fen.fen['turn'] == 'b':
                '''raiseError'''
                raise Exception(f'illegal move >> {crd0_inpNotation}{crd1_inpNotation} is a square occupied by the white piece "{matrix_value}"')
            elif matrix_value.islower() and fen.fen['turn'] == 'p':
                '''raiseError'''
                raise Exception(f'illegal move >> {crd0_inpNotation}{crd1_inpNotation} is a square occupied by the black piece "{matrix_value}"')
        else:
            if matrix_value != self.board.blank:
                '''raiseError'''
                raise Exception(f'"x" not correctly inserted >> must be used in a move with an occupied crd')
            
    def find_crv(self, piece: Type[Piece]) -> None:

        for dir in piece.direction:
            for sense in piece.sense:

                step = 0
                while step < piece.distancing:
                    step += 1

                    crv0 = self.crd[0] + step*sense*dir[0]
                    crv1 = self.crd[1] + step*sense*dir[1]

                    if not (self.board.rows - 1) >= crv0 >= 0 or not (self.board.columns - 1) >= crv1 >= 0:
                        break

                    if self.board.matrix[crv0][crv1] == piece.name:
                        self.crv = (crv0, crv1)
                        break
                    elif self.board.matrix[crv0][crv1] != self.board.blank:
                        break
    
    def crv_validation(self, inp: str) -> None:

        if len(self.crv) == 0:
            '''raiseError'''
            raise Exception('illegal move >> empty crv')
        
        elif len(self.crv) == 1:
            pass
        
        else:
            self.__multiplicity_crv(inp)

    def __multiplicity_crv(self, inp):
            
        crv0, crv1 = zip(*self.crv)
        if re.search(r'.[a-h][1-8]x?[a-h][1-8].*', inp):
            '''column and row case'''
            crv0_inp, crv1_inp = self.convert_CrdInpNotation(inp[1], inp[2])
            if not any(map(lambda x: x[0] == crv0_inp, self.crv)):
                '''raiseError'''
                raise Exception(f'there is no crv at column {inp[1]}')
            if not any(map(lambda x: x[1] == crv1_inp, self.crv)):
                '''raseError'''
                raise Exception(f'there is no crv at row {inp[2]}')
            
            for tup in self.crv:
                if tup == (crv0_inp, crv1_inp):
                    self.crv.clear()
                    self.crv = tup
                    break
        
        elif re.search(r'.[a-h]x?[a-h][1-8].*', inp):
            '''column case'''
            crv0_inp = self.convert_CrdInpNotation(inp[1])
            if not any(map(lambda x: x[0] == crv0_inp, self.crv)):
                '''raseError'''
                raise Exception(f'there is no crv at column {inp[1]}')
            if crv0.count(crv0_inp) > 1:
                '''raseError'''
                raise Exception(f'ambiguos move in column {inp[1]}')
            
            for tup in self.crv:
                if tup[0] == crv0_inp:
                    self.crv.clear()
                    self.crv = tup
                    break
        
        elif re.search(r'.[1-8]x?[a-h][1-8].*', inp):
            '''row case'''
            crv1_inp = self.convert_CrdInpNotation(inp[1])
            if not any(map(lambda x: x[1] == crv1_inp, self.crv)):
                '''raiseError'''
                raise Exception(f'there is no crv at row {inp[1]}')
            if crv1.count(crv1_inp) > 1:
                '''raiseError'''
                raise Exception(f'ambiguos move in row {inp[1]}')
        
            for tup in self.crv:
                if tup[1] == crv1_inp:
                    self.crv.clear()
                    self.crv = tup
                    break

        else:
            '''raiseError'''
            raise Exception('ambiguos move >> needed a crv input')
    
    def update_matrix(self, piece: Type[any]) -> None:
        
        self.board.matrix[self.crd[0]][self.crd[1]] = piece.name
        self.board.matrix[self.crv[0][0]][self.crv[0][1]] = self.board.blank

    @staticmethod
    def slice_inputCrd(inp: str) -> str:
        crd_index = list(re.finditer(r'[a-h][1-8]', inp)).pop().start()
        crd0_inpNotation = inp[crd_index]
        crd1_inpNotation = inp[crd_index + 1]
        return crd0_inpNotation, crd1_inpNotation
    
    @staticmethod
    def slice_inputCapture(inp: str) -> bool:
        if 'x' in inp:
            capture = True
        else:
            capture = False
        return capture

    @staticmethod
    def slice_inputName(inp: str) -> str:
        name = inp[0]
        return name

    @staticmethod
    def convert_CrdInpNotation(inp1: str=None, inp2: str=None) -> int:

        if inp1 is not None and inp2 is not None:
            cr0 = ord(inp1) - ord('a')
            cr1 = int(inp2) - 1
            return cr0, cr1
        elif inp1.isalpha():
            cr0 = ord(inp1) - ord('a')
            return cr0
        else:
            cr1 = int(inp1) - 1
            return cr1

        
