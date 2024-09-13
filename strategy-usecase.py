from abc import ABCMeta, abstractmethod

class GameCharacter():
    position = [0,0]

    @classmethod
    def move(cls, movement_style):
        """movement style decided by the client"""
        movement_style(cls.position)

class IMove(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __call__():
        """implementors must select default method"""

class Walking(IMove):
    @staticmethod
    def walk(position):
        position[0] += 1
        print(f'im walking, position {position}')

    __call__ = walk

class Running(IMove):
    @staticmethod
    def run(position):
        position[0] += 2
        print(f'im running, position {position}')

    __call__ = run

class Crawling(IMove):
    @staticmethod
    def craw(position):
        position[0] += 0.5
        print(f'im crawling, position {position}')

    __call__ = craw

CHARACTER = GameCharacter()
CHARACTER.move(Walking())
CHARACTER.move(Crawling())
CHARACTER.move(Running())
