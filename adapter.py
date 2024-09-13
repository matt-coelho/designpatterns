# sometimes classes have been writen and you dont have the option to modify their interface for your needs
# like when the method youre calling is not viable to modify directly
# the adapter is used when you have an existing interface that doenst directly map to an interface that the client requires
# so then you create the adapter that has a similar functional role but with a new compatible interface
from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    """interface for an object"""
    @staticmethod
    @abstractmethod
    def method_a():
        """an abstract method"""

class ClassA(IA):
    def method_a(self):
        print("method A")

class IB(metaclass=ABCMeta):
    """an interface for an object"""
    @staticmethod
    @abstractmethod
    def method_b():
        """an abstract method"""

class ClassB(IB):
    def method_b(self):
        print("method B")

class ClassBAdapter(IA):
    """class B does not have a method_a"""
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        self.class_b.method_b()

# ITEMS = [ClassA(), ClassB()]
# for item in ITEMS:
#     if isinstance(item, ClassB):
#         item.method_b()
#     else:
#         item.method_a()

ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()