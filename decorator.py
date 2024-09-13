# padrao estrutural que permite incluir responsabilidades adicionais a um objeto em tempo de execucao

from abc import ABCMeta, abstractmethod

class IValue(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__():
        """override the object to return the value attribute by default"""
class Value(IValue):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
class Sub(IValue):
    def __init__(self, val1, val2):
        val1 = getattr(val1, 'value', val1)
        val2 = getattr(val2, 'value', val2)
        self.value = val1 - val2

    def __str__(self):
        return str(self.value)
class Add(IValue):
    def __init__(self, val1, val2):
        val1 = getattr(val1, "value", val1)
        val2 = getattr(val2, "value", val2)
        self.value = val1 + val2
    def __str__(self):
        return str(self.value)

A = Value(1)
B = Value(2)
C = Value(5)

print(Add(A, B))