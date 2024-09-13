# decorator uses composition, different from extension/inheritance
# uma funcionalidade é agregada de forma dinamica, sem alterar a estrutura original do objeto envolto
# quando da extensao/heranca, é feita a expecializacao do objeto original, que permite reutilizar funcionalidades existentes
# so que envolvendo uma relacao hierarquica entre as classes
from abc import ABCMeta, abstractmethod

class IComponent(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method():
        """to implement"""

class Component(IComponent):
    """a component that can be decorated or not"""
    def method(self):
        return 'component method'

class Decorator(IComponent):
    def __init__(self, obj):
        self.object = obj
    def method(self):
        return f"decorator method({self.object.method()})"

COMPONENT = Component()
print(COMPONENT.method())
print(Decorator(COMPONENT).method())
print(Decorator(Decorator(COMPONENT)).method())

