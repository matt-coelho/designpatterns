# good for when creating new objects require more resources you want to use or are available
# by just creating a copy of any existing object already in memory, that takes lots or resources to be created
# the method of copy can vary, be shallow or deep

import copy
from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):
    """interface with clone method"""

    @staticmethod
    @abstractmethod
    def clone():
        """"
        The clone, deep or shallow
        up to the developer how to implement the details in the concrete class
        """


class MyClass(IPrototype):
    """a concrete class"""

    def __init__(self, field):
        self.field = field

    def clone(self):
        """using the shallow copy technique"""
        return type(self)(self.field  # a shallow copy is returned
                          )

    def clone2(self):
        return type(self)(self.field.copy())  # returns a shallow copy, but two levels deep

    def clone3(self):
        return type(self)(copy.deepcopy(self.field))  # return a deep recursive copy, needs to import copy

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"


Object1 = MyClass([1, 2, 3, 4, 5])  # creates an object containing a list
print(f"Object1 {Object1}")
print('copies')
Object2 = Object1.clone()
Object2.field[1] = 101

# comparing
print(f"Object1 {Object1}")
print(f"Object2 {Object2}")
print("*" * 10)

Object3 = MyClass([6, 7, 8, 9])  # creates an object containing a list
print(f"Object3 {Object3}")
print('copies')
Object4 = Object3.clone2()
Object4.field[1] = 101

# comparing
print(f"Object3 {Object3}")
print(f"Object4 {Object4}")
print("*" * 10)

Object5 = MyClass([0, [12, 13, 14], 2, 3])  # creates an object containing a list
print(f"Object5 {Object5}")
print('copies')  # copy2 wont work here, wont go as deep
Object6 = Object5.clone2()
Object6.field[1][1] = 101

# comparing
print(f"Object5 {Object5}")
print(f"Object6 {Object6}")

print("*" * 10)

Object7 = MyClass([0, [12, 13, 14], 2, 3])  # creates an object containing a list
print(f"Object7 {Object7}")
print('copies')  # copy2 wont work here, wont go as deep
Object8 = Object7.clone3()
Object8.field[1][1] = 101

# comparing
print(f"Object7 {Object7}")
print(f"Object8 {Object8}")
