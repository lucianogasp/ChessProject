# CHESS PROJECT 2.2

import re

class Move:

    def __init__(self, piece_name):
        self._crd = list()
        self._crv = list()
        self.__regex_generic = rf'^(?:[{piece_name}][a-h]?[1-8]?x?|[a-h]x)?[a-h][1-8](?:=[A-Z])?(?:\+|\+\+|#)?$'
        
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

    def input_move(self) -> str:
        return input('Digite seu lance: ').strip()

    def input_validation(self, inp: str, regexp: str=None) -> None:

        if regexp is None:
            regexp = self.__regex_generic

        verify = re.search(regexp, inp)
        if not verify:
            '''raise Error'''

    def verify_crv(self, inp) -> None:
        
        if len(self.crv) == 0:
            '''raise Error'''
            pass
        elif len(self.crv) == 1:
            '''matrix update'''
            pass
        else:
            '''CRV's multiplicity logic'''
            crv0, crv1 = zip(*self.crv)
            rep0 = set()
            rep1 = set()
            for (first, second) in self.crv:
                if crv0.count(first) > 1:
                    rep0.add(first)
                if crv1.count(second) > 1:
                    rep1.add(second)
            
            if len(rep0) > 0 and len(rep1) > 0:
                '''regex context logic - col e row'''
                regex_context = re.compile(r'^.[a-h][1-8].+')
                self.input_validation(inp, regex_context)

                

            elif len(rep0) > 0:
                '''regex context logic - col'''
                regex_context = re.compile(r'^.[1-8].+')
                self.input_validation(inp, regex_context)

            elif len(rep1) > 0:
                '''regex context logic - row'''
                regex_context = re.compile(r'^.[a-h].+')
                self.input_validation(inp, regex_context)

            else:
                '''...'''
                regex_context = re.compile(r'^.(?:[a-h]|[1-8]|[a-h][1-8]).+')
                self.input_validation(inp, regex_context)
    
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
