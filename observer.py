"""
follows the publish/subscribe concept, a subscriber, subscribes to a publisher, the publisher notify the subscribers
when necessary.
um objeto chamado sujeito(observavel) gerencia uma lista de dependentes, observadores e os notifica automaticamente
de qualquer mudanca de estado interna, chamando um de seus metodos.
o observador armazana um estado que deve ser consistente com o sujeito e so deve armazenar o que for necessario para
seu proposito
"""

from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):
    """the subject interface"""
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """subscribe method to implement"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """unsubscribe method to implement"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """notify method to implement"""

class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)

class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args):
        """receive notifications to implement"""

class Observer(IObserver):
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, *args):
        print(f'observer id: {id(self)} received {args}')

SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT)
OBSERVER_B = Observer(SUBJECT)

SUBJECT.notify("first notification ", [1,2,3])

SUBJECT.unsubscribe(OBSERVER_B)
SUBJECT.notify('second notification ', {'a': 1, 'b': 2, 'c': 3})
