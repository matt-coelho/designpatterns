"""
describes an accept method, that a different object, called visitor, will use to traverse through the existing object hierarch
and read the internal attributes of an object.
could be used to output different versions of document, but more suited to objects that may be members of a hierarchy
"""
from abc import ABCMeta, abstractmethod

class IVisitor(metaclass=ABCMeta):
    """interface for the visitors to implement"""

    @staticmethod
    @abstractmethod
    def visit(element):
        """visitors visit elements/objects within the application"""

class IVisitable(metaclass=ABCMeta):
    """interface the concrete objects should implement that allows the visitor to traverse a hierarchical structure"""
    @staticmethod
    @abstractmethod
    def accept(visitor):
        """the visitor traverses and accesses each object through this method"""

class Element(IVisitable):
    """object that can be part of any hierarchy"""
    def __init__(self, name, value, parent=None):
        self.name = name
        self.value = value
        self.elements = set()
        if parent:
            parent.elements.add(self)

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)
        visitor.visit(self)

ELEMENT_A = Element('a', 101)
ELEMENT_B = Element('b', 305, ELEMENT_A)
ELEMENT_C = Element('c', 185, ELEMENT_A)
ELEMENT_D = Element('d', -30, ELEMENT_B)

"""
agora ao inves de alterar a classe Element para suportar operacoes personalizadas,
podemos usar o metodo accept que foi implementado na mesma classe
"""

class PrintElementNamesVisitor(IVisitor):
    @staticmethod
    def visit(element):
        print(element.name)

ELEMENT_A.accept(PrintElementNamesVisitor)

class CalculateElementTotalsVisitor(IVisitor):
    total_value = 0

    @classmethod
    def visit(cls, element):
        cls.total_value += element.value
        return cls.total_value

TOTAL = CalculateElementTotalsVisitor()
ELEMENT_A.accept(CalculateElementTotalsVisitor)
print(TOTAL.total_value)
