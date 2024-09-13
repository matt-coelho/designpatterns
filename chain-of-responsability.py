"""
used to achieve loose coupling in software design
um objeto é passado a um sucessor e dependendo de uma logica sera ou nao repassado a outro sucessor e processado
esse processo de repasse a sucessor é chamado de 'chain'
o objeto passado (paylod) nao sabe por quais sucessores será passado
"""

import random
from abc import ABCMeta, abstractmethod

class IHandler(metaclass=ABCMeta):
    """interface the handlers should implement"""
    @staticmethod
    @abstractmethod
    def handle(payload):
        """to be implemented"""

class Successor1(IHandler):
    @staticmethod
    def handle(payload):
        print(f'successor 1 payload = {payload}')
        test = random.randint(1,2)
        if test == 1:
            payload = payload + 1
            payload = Successor1().handle(payload)

        if test == 2:
            payload = payload - 1
            payload = Successor2().handle(payload)
        return payload

class Successor2(IHandler):
    @staticmethod
    def handle(payload):
        print(f'successor 2 payload = {payload}')
        test = random.randint(1,3)
        if test == 1:
            payload = payload * 2
            payload = Successor1().handle(payload)

        if test == 2:
            payload = payload / 2
            payload = Successor2().handle(payload)
        return payload

class Chain():
    """chain with a default first successor"""
    @staticmethod
    def start(payload):
        return Successor1().handle(payload)


CHAIN = Chain()
PAYLOAD = 1
OUT = CHAIN.start(PAYLOAD)
print(f'finished result {OUT}')
