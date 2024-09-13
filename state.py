"""
nao deve ser confundido com o estado de um objeto
o comportamento do estado de um objeto é encapsulado na subclasse que é dinamicamente assinalada
"""
from abc import ABCMeta, abstractmethod
import random

class IState(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__():
        """set the default method"""

class ConcreteStateA(IState):
    def __str__(self):
        return 'concrete state A'

class ConcreteStateB(IState):
    def __str__(self):
        return 'concrete state B'

class ConcreteStateC(IState):
    def __str__(self):
        return 'concrete state C'

class Context():
    """object whose behavior will change"""
    def __init__(self):
        self.state_handles = [ConcreteStateA(), ConcreteStateB(), ConcreteStateC()]
        self.handle = None

    def request(self):
        self.handle = self.state_handles[random.randint(0,2)]
        return self.handle

CONTEXT = Context()
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())
print(CONTEXT.request())