import sys
from abc import ABCMeta, abstractmethod

class IDispenser(metaclass=ABCMeta):
    """methods to implement"""
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        """to implement, set the next handler"""

    @staticmethod
    @abstractmethod
    def handle(amount):
        """handle the event"""

class Dispenser50(IDispenser):
    def __init__(self):
        self._successor = None
        self._to_dispense = 50

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= self._to_dispense:
            num = amount // self._to_dispense
            remainder = amount % self._to_dispense
            print(f'dispensing {num} {self._to_dispense} notes')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)

class Dispenser20(IDispenser):
    def __init__(self):
        self._successor = None
        self._to_dispense = 20

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= self._to_dispense:
            num = amount // self._to_dispense
            remainder = amount % self._to_dispense
            print(f'dispensing {num} {self._to_dispense} notes')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser10(IDispenser):
    def __init__(self):
        self._successor = None
        self._to_dispense = 10

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= self._to_dispense:
            num = amount // self._to_dispense
            remainder = amount % self._to_dispense
            print(f'dispensing {num} {self._to_dispense} notes')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser5(IDispenser):
    def __init__(self):
        self._successor = None
        self._to_dispense = 5

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= self._to_dispense:
            num = amount // self._to_dispense
            remainder = amount % self._to_dispense
            print(f'dispensing {num} {self._to_dispense} notes')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser2(IDispenser):
    def __init__(self):
        self._successor = None
        self._to_dispense = 2

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= self._to_dispense:
            num = amount // self._to_dispense
            remainder = amount % self._to_dispense
            print(f'dispensing {num} {self._to_dispense} notes')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Dispenser1(IDispenser):
    def __init__(self):
        self._successor = None
        self._to_dispense = 1

    def next_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        if amount >= self._to_dispense:
            num = amount // self._to_dispense
            remainder = amount % self._to_dispense
            print(f'dispensing {num} {self._to_dispense} notes')
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)

class ATMDispenserChain():
    def __init__(self):
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()
        self.chain4 = Dispenser5()
        self.chain5 = Dispenser2()
        self.chain6 = Dispenser1()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)
        self.chain3.next_successor(self.chain4)
        self.chain4.next_successor(self.chain5)
        self.chain5.next_successor(self.chain6)


ATM = ATMDispenserChain()
AMOUNT = int(input('enter amount to withdraw: '))
if AMOUNT < 1 or AMOUNT % 1 != 0:
    print('amount should be positive and multiple of 1')
    sys.exit()
ATM.chain1.handle(AMOUNT)
print('done')