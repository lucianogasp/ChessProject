# CHESS PROJECT 2.2

import re

class Move:

    def __init__(self):
        self._crd = list()
        self._crv = list()
        
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
    def crv(self, value: int) -> None:
        self.crv.append(value)

    def input_move(self):
        return input('Digite seu lance: ').strip()

    def input_validation(self, inp):

        regex = re.compile(r'')

        pass
    
    def find_crv(self):
        pass
'''
        for k in self.piece.k:          # Define direção
            for j in self.piece.j:          # Define sentido

                flag = i = 0

                while flag < self.piece.flag:   # Define o passo do movimento
                    i += 1

                    crv0 = self.crd[0] + i*j*k[0]
                    crv1 = self.crd[1] + i*j*k[1]

                    if not (self.rows - 1) >= crv0 >= 0 or not (self.columns - 1) >= crv1 >= 0:
                        break

                    if self.matrix[crv0][crv1] == self.piece.name:
                        self.crv.append(crv0)
                        self.crv.append(crv1)
                        break
                    elif self.matrix[crv0][crv1] != self.blank:
                        break

                    flag += 1
'''
