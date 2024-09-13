# __call__ method permite definir um metodo padrao para execucao de uma classe

from abc import ABCMeta, abstractmethod

class IState(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __call__():
        """set defaul method"""

class Started(IState):
    @staticmethod
    def method():
        print('task started')

    __call__ = method

class Running(IState):
    @staticmethod
    def method():
        print('tasl running')

    __call__ = method

class Finished(IState):
    @staticmethod
    def method():
        print('task finished')

    __call__ = method

class Context():
    def __init__(self):
        self.state_handles = [
            Started(),
            Running(),
            Finished()
        ]
        self._handle = iter(self.state_handles)

    def request(self):
        try:
            self._handle.__next__()()
        except StopIteration:
            # resets so it loops
            self._handle = iter(self.state_handles)

CONTEXT = Context()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
CONTEXT.request()
