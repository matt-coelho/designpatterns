"""
a comunicacao entre objetos ocorre atraves do mediador ao inves de diretamente e permite comunicacao multi-direcional
"""

class Colleague1():
    @staticmethod
    def method_1():
        return "colleague1 specific data"

class Colleague2():
    @staticmethod
    def method_2():
        return "colleague2 specific data"

class Mediator():
    def __init__(self):
        self.colleague1 = Colleague1()
        self.colleague2 = Colleague2()

    def colleague1_method(self):
        return self.colleague1.method_1()

    def colleague2_method(self):
        return self.colleague2.method_2()


# colleague 1 wants data from colleague 2
MEDIATOR = Mediator()
DATA = MEDIATOR.colleague2_method()
print(f'colleague1 <--> {DATA}')

# colleague 2 wants data from colleague 1
DATA = MEDIATOR.colleague1_method()
print(f'colleague2 <--> {DATA}')
