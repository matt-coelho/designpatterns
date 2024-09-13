"""
similar to state but the client passes in the algorithm that the context should run
a good way to differentiate them is to consider whether the state of the context is choosing the algorithm at runtime
or the algorithm is being passed into it
"""

from abc import ABCMeta, abstractmethod

class Context():
    """object whose behavior will change"""
    @staticmethod
    def request(strategy):
        return strategy()


class IStrategy(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def __str__():
        """implement the dunder method"""

class ConcreteStrategyA(IStrategy):
    def __str__(self):
        return 'i am strategy A'

class ConcreteStrategyB(IStrategy):
    def __str__(self):
        return 'i am strategy B'

class ConcreteStrategyC(IStrategy):
    def __str__(self):
        return 'i am strategy C'

CONTEXT = Context()

print(CONTEXT.request(ConcreteStrategyA))
print(CONTEXT.request(ConcreteStrategyB))
print(CONTEXT.request(ConcreteStrategyC))
