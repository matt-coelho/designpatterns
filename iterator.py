"""
commonly contains two methods, next (object/collection) and has_next(boolean). next(), at minimum

beneficia o cliente que pode usar uma colecao de objetos sem precisar conhecer
sua representacao interna ou estutura de dados
# an interable can be instantiated using the iter() method

names = ['sean', 'cosmo', 'emmy']
iterator = names.__iter__()  # /or # iterator = iter(names)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
"""
from abc import ABCMeta, abstractmethod

class IIterator(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def has_next():
        """returns boolean whether at end of collection or not"""

    @staticmethod
    @abstractmethod
    def next():
        """returns the object in collection"""

class Iterable(IIterator):
    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate
        raise Exception("AtEndOfIteratorException", "At end of iterator")

    def has_next(self):
        return self.index < len(self.aggregates)

class IAggregate(metaclass=ABCMeta):
    """interface that aggregate should implement"""
    @staticmethod
    @abstractmethod
    def method():
        """to implement"""

class Aggregate(IAggregate):
    """concrete object"""
    @staticmethod
    def method():
        print('method invoked')

AGGREGATES = [Aggregate(), Aggregate(), Aggregate(), Aggregate()]
ITERABLE = Iterable(AGGREGATES)

while ITERABLE.has_next():
    ITERABLE.next().method()
