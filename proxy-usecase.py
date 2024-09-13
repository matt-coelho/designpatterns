import random
from abc import ABCMeta, abstractmethod

class IProteus(metaclass=ABCMeta):
    """mythological character that can change to many forms"""

    @staticmethod
    @abstractmethod
    def tell_me_the_future():
        """changes form"""

    @staticmethod
    @abstractmethod
    def tell_me_your_form():
        """prints its form"""

class Leopard(IProteus):
    name = 'Leopard'

    @classmethod
    def tell_me_your_form(cls):
        print(f"I'm the form of a {cls.name}")

    def tell_me_the_future(self):
        self.__class__ = Serpent if random.randint(0, 1) else Lion

class Serpent(IProteus):
    name = 'Serpent'

    @classmethod
    def tell_me_your_form(cls):
        print(f"I'm the form of a {cls.name}")

    def tell_me_the_future(self):
        self.__class__ = Leopard if random.randint(0, 1) else Lion

class Lion(IProteus):
    name = 'Lion'

    @classmethod
    def tell_me_your_form(cls):
        print(f"I'm the form of a {cls.name}")

    def tell_me_the_future(self):
        self.__class__ = Leopard if random.randint(0, 1) else Serpent

PROTEUS = Lion()
PROTEUS.tell_me_your_form()
PROTEUS.tell_me_the_future()
PROTEUS.tell_me_your_form()
PROTEUS.tell_me_the_future()
PROTEUS.tell_me_your_form()
PROTEUS.tell_me_the_future()
PROTEUS.tell_me_your_form()
PROTEUS.tell_me_the_future()
PROTEUS.tell_me_your_form()
PROTEUS.tell_me_the_future()
