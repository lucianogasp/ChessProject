# CHESS PROJECT 2.2

from typing import Type
from Modules import Board, Piece, InputMove

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
    
    @crd.deleter
    def crd(self) -> None:
        self._crd.clear()
    
    @property
    def crv(self) -> list:
        return self._crv
    
    @crv.setter
    def crv(self, value: tuple) -> None:
        self._crv.append(value)
    
    @crv.deleter
    def crv(self) -> None:
        self._crv.clear()
            
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
    
    def crv_validation(self, inp: str, move: Type[InputMove]) -> None:

        if len(self.crv) == 0:
            '''raiseError'''
            raise Exception('illegal move >> empty crv')
        
        elif len(self.crv) == 1:
            pass
        
        else:
            self.__multiplicity_crv(inp, move)
    
    def __multiplicity_crv(self, inp, move: Type[InputMove]):

        crv_column, crv_row = zip(*self.crv)
        crv_input = move.slice_inputCrv(inp)

        if crv_input is None:
            '''raiseError'''
            raise Exception('ambiguos move >> needed a crv input')

        elif crv_input.isalpha():

            crv0 = move.convert_CrInpNotation(crv_input)
            if not crv0 in crv_column:
                '''raiseError'''
                raise Exception(f'there is no crv at column {crv_input}')
            if crv_column.count(crv0) > 1:
                '''raiseError'''
                raise Exception(f'ambiguos move in column {crv_input}')

            new_crv, = tuple(filter(lambda x: crv0 == x[0], self.crv))
            del self.crv
            self.crv = new_crv

        elif crv_input.isdigit():

            crv1 = move.convert_CrInpNotation(crv_input)
            if not crv1 in crv_row:
                '''raiseError'''
                raise Exception(f'there is no crv at row {crv_input}')
            if crv_row.count(crv1) > 1:
                '''raiseError'''
                raise Exception(f'ambiguos move in row {crv_input}')
            
            crv0 = [tup[0] for tup in self.crv if tup[1] == crv1]
            crv0, = crv0
            
            if crv_column.count(crv0) <= 1:
                '''raiseError'''
                raise Exception('by convention the crv input must be mentioned by column instead of row')
    
            new_crv, = tuple(filter(lambda x: crv1 == x[1], self.crv))
            del self.crv
            self.crv = new_crv

        elif crv_input.isalnum():

            crv0, crv1 = move.convert_CrInpNotation(crv_input)
            if not (crv0, crv1) in self.crv:
                '''raiseError'''
                raise Exception(f'there is no crv at {crv_input}')
            if crv_column.count(crv0) <= 1:
                '''raiseError'''
                raise Exception('by convention the crv input must be mentioned by column instead of column and row')
            if crv_row.count(crv1) <= 1:
                '''raiseError'''
                raise Exception('by convention the crv input must be mentioned by row instead of column and row')
    
            new_crv, = tuple(filter(lambda x: (crv0, crv1) == x, self.crv))
            del self.crv
            self.crv = new_crv

    def update_matrix(self, piece: Type[Piece]) -> None:
        
        self._board.matrix[self.crd[0]][self.crd[1]] = piece.name
        self._board.matrix[self.crv[0][0]][self.crv[0][1]] = self._board.blank
