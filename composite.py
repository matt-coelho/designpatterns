# util para gerenciamento hierarquico
# permite representar entidades individuais e grupos como uma mesma coisa
# permite compor objetos em uma estrutura de arvore alteravel

from abc import ABCMeta, abstractmethod
from multiprocessing.process import parent_process


class IComponent(metaclass=ABCMeta):
    """"component interface describing the common fields and methods of leaves and composites"""
    reference_to_parent = None

    @staticmethod
    @abstractmethod
    def method():
        """"each leaf and composite should implement"""

    @staticmethod
    @abstractmethod
    def detach():
        """called before a leaf is attached to a composite"""

class Leaf(IComponent):
    """"leaf can be added to composite but not to a leaf"""
    def method(self):
        parent_id = (id(self.reference_to_parent) if self.reference_to_parent is not None else None)
        print(f"leaf id {id(self)} parent id {parent_id}")

    def detach(self):
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)

class Composite(IComponent):
    """"contains leafs and composites"""
    def __init__(self):
        self.components = []

    def method(self):
        parent_id = (id(self.reference_to_parent) if self.reference_to_parent is not None else None)

        print(f"composite id {id(self)} parent id {parent_id} components {len(self.components)}")

        for component in self.components:
            component.method()

    def attach(self, component):
        """detach leaf/composite from this self.components"""
        component.detach()
        component.reference_to_parent = self
        self.components.append(component)

    def delete(self, component):
        self.components.remove(component)

    def detach(self):
        """detaching this composite from its parent"""
        if self.reference_to_parent is not None:
            self.reference_to_parent.delete(self)
            self.reference_to_parent = None

LEAF_A = Leaf()
LEAF_B = Leaf()
COMPOSITE_1 = Composite()
COMPOSITE_2 = Composite()

print(f"leaf a id {id(LEAF_A)}")
print(f"leaf b id {id(LEAF_B)}")
print(f"composite 1 id {COMPOSITE_1}")
print(f"composite 2 id {COMPOSITE_2}")

COMPOSITE_1.attach(LEAF_A)
COMPOSITE_2.attach(LEAF_B)

COMPOSITE_2.attach(COMPOSITE_1)

LEAF_B.method()
COMPOSITE_2.method()