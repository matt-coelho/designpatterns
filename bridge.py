# bridge patter é similar ao adapter mas, a abordagem é atraves da refatoracao de um codigo existente
# é o processo de separacao entre abstracao e implementacao com isso criando varias novas formas de utilizar as classes
# a aplicacao do padrao deve usar composicao ao inves de heranca

from abc import ABCMeta, abstractmethod

class IAbstraction(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(*args):
        """"the method handler"""

class RefinedAbstractionA(IAbstraction):
    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)

class RefinedAbstractionB(IAbstraction):
    def __init__(self, implementer):
        self.implementer = implementer()

    def method(self, *args):
        self.implementer.method(*args)

class IImplementer(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method(*args: tuple) -> None:
        print(args)

class ConcreteImplementerA(IImplementer):
    @staticmethod
    def method(*args: tuple)->None:
        print(args)

class ConcreteImplementerB(IImplementer):
    @staticmethod
    def method(*args: tuple)->None:
        for arg in args:
            print(arg)


REFINEDABSTRACTION_A = RefinedAbstractionA(ConcreteImplementerA)
REFINEDABSTRACTION_A.method('a','b', 'c')

REFINEDABSTRACTION_B = RefinedAbstractionB(ConcreteImplementerB)
REFINEDABSTRACTION_B.method('a', 'b', 'c')
