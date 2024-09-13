# use quando quiser separar uma solucao onde a abstracao é altamente acoplada, para separar em partes conceituais menores

from abc import ABCMeta, abstractmethod

class IShape(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def draw():
        """the method that will be handled at the shapes implementer"""

class IShapeImplementer(metaclass=ABCMeta):
    """"shape implementer"""
    @staticmethod
    @abstractmethod
    def draw_implementation():
        """the method the refined abstraction will implement"""

class Square(IShape):
    """square refined abstraction"""
    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()

class Circle(IShape):
    """circle refined abstraction"""
    def __init__(self, implementer):
        self.implementer = implementer()

    def draw(self):
        self.implementer.draw_implementation()

class SquareImplementer(IShapeImplementer):
    """square implementer"""
    def draw_implementation(self):
        print("*"*11)
        print("*"," "*8, "*")
        print("*", " " * 8, "*")
        print("*", " " * 8, "*")
        print("*", " " * 8, "*")
        print("*"*11)

class CircleImplementer(IShapeImplementer):
    """circle implementer"""
    def draw_implementation(self):
        print("    ******")
        print("  **      **")
        print(" *          *")
        print("*            *")
        print("*            *")
        print(" *          *")
        print("  **      **")
        print("    ******")

CIRCLE = Circle(CircleImplementer)
CIRCLE.draw()

SQUARE = Square(SquareImplementer)
SQUARE.draw()