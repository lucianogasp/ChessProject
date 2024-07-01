# CHESS PROJECT 2.2

from typing import Type
from Modules import Board, Piece

import re

class EngineMove:

    def __init__(self, board: Type[Board]) -> None:

        self._crd = list()
        self._crv = list()

        self._board = board
        
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
            
    def find_crv(self, piece: Type[Piece]) -> None:

        for dir in piece.direction:
            for sense in piece.sense:

                step = 0
                while step < piece.distancing:
                    step += 1

                    crv0 = self.crd[0] + step*sense*dir[0]
                    crv1 = self.crd[1] + step*sense*dir[1]

                    if not (self._board.rows - 1) >= crv0 >= 0 or not (self._board.columns - 1) >= crv1 >= 0:
                        break

                    if self._board.matrix[crv0][crv1] == piece.name:
                        self.crv = (crv0, crv1)
                        break
                    elif self._board.matrix[crv0][crv1] != self._board.blank:
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
    
    def update_matrix(self, piece: Type[Piece]) -> None:
        
        self._board.matrix[self.crd[0]][self.crd[1]] = piece.name
        self._board.matrix[self.crv[0][0]][self.crv[0][1]] = self._board.blank
