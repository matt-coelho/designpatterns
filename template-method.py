"""
uma classe abstrata (template) é criada e contem o template method, que é uma serie de instrucoes, combinacao de metodos
abstratos e metodos gancho.
metodos abstrados devem ser sobrescritos nas subclasses que herdam da classe template
metodos gancho tem um comportamento padrao, corpo normalmente vazio na classe abstrata e pode ser sobrescrito em subclasses
descreve o comportamento de um metodo e como seus metodos internos devem ser chamados
"""
from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    """template clas"""
    @staticmethod
    def step_one():
        """hook, normally empty"""

    @staticmethod
    @abstractmethod
    def step_two():
        """abstract, must be overridden"""

    @staticmethod
    def step_three():
        """hook, can also contain default behavior"""

    @classmethod
    def template_method(cls):
        """template method the subclass will call, does not need to be overridden"""
        cls.step_one()
        cls.step_two()
        cls.step_three()

class ConcreteClassA(AbstractClass):
    @staticmethod
    def step_two():
        print('class a, method two, overridden')

class ConcreteClassB(AbstractClass):
    @staticmethod
    def step_one():
        print('class b, method one, overridden')

    @staticmethod
    def step_two():
        print('class b, method two, overridden')

    @staticmethod
    def step_three():
        print('class b, method three, overridden')

CLASS_A = ConcreteClassA()
CLASS_A.template_method()

CLASS_B = ConcreteClassB()
CLASS_B.template_method()
