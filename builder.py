"""
similar a factory, mas o processo de criacao do objeto a ser retornado é mais complexo
"""
from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def build_part_a():
        """build part A"""
    @staticmethod
    @abstractmethod
    def build_part_b():
        """build part B"""
    @staticmethod
    @abstractmethod
    def build_part_c():
        """build part C"""

    @staticmethod
    @abstractmethod
    def get_result():
        """the final product"""

class Product():
    def __init__(self):
        self.parts = []

class Builder(IBuilder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product

class Director():
    @staticmethod
    def construct():
        return Builder().build_part_a().build_part_b().build_part_c().get_result()

PRODUCT = Director.construct()
print(PRODUCT.parts)
