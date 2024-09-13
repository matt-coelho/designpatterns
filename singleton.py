"""
usado quando se quer que apenas uma versao de um objeto exista
"""
import copy

class Singleton:
    """the singleton class""" # has no reference to self
    value = []

    def __new__(cls):  # this forces the return of the same id for the class, a singleton
        return cls # also prevents __init__ to being called

    # def __init__(self):
    #   print('in init')

    @staticmethod
    def static_method():
        """use if no inner variable required"""

    @classmethod
    def class_method(cls):
        """use @classmethod to access class level variables"""
        print(cls.value)


print(f"id(Singleton)\t={id(Singleton)}")

Obj1 = Singleton()
print(f"id(Obj1)\t={id(Obj1)}")

Obj2 = copy.deepcopy(Obj1)
print(f"id(Obj2)\t={id(Obj2)}")

Obj3 = Singleton()
print(f"id(Obj3)\t={id(Obj3)}")