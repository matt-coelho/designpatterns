from abc import ABCMeta, abstractmethod

class IComponent(metaclass=ABCMeta):
    """each component will implement"""
    @staticmethod
    @abstractmethod
    def notify(message):
        """required notify method"""

    @staticmethod
    @abstractmethod
    def receive(message):
        """required receive method"""

class Component(IComponent):
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def notify(self, message):
        print(f"{self._name} >> out >> {message}" )
        self._mediator.notify(message, self)

    def receive(self, message):
        print(f"{self._name} << in << {message}")

class Mediator():
    def __init__(self):
        self._components = set()

    def add(self, component):
        self._components.add(component)

    def notify(self, message, originator):
        """add components except for the originator"""
        for component in self._components:
            if component != originator:
                component.receive(message)

MEDIATOR = Mediator()
COMPONENT1 = Component(MEDIATOR, "COMP1")
COMPONENT2 = Component(MEDIATOR, "COMP2")
COMPONENT3 = Component(MEDIATOR, "COMP3")
MEDIATOR.add(COMPONENT1)
MEDIATOR.add(COMPONENT2)
MEDIATOR.add(COMPONENT3)

COMPONENT1.notify('data A')
COMPONENT2.notify('data B')
COMPONENT3.notify('data C')