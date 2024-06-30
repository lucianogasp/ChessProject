# CHESS PROJECT 2.2 - TEST

from abc import ABC, abstractmethod

class Abs(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def name(self):
        pass

    def ola(self):
        print('olá')

class Concret(Abs):

    def __init__(self):
        self._name = 1

    @property
    def get(self):
        return self._name

    @get.setter
    def name(self, new_name):
        self._name += 1

    def ola2(self):
        print('olá2')


obj = Concret()

print(obj.get)
obj.name = 1
print(obj.get)

print(type(float('inf')))
