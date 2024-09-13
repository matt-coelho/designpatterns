# padrao de projeto comportamental em que existe uma abstrancao entre o objeto que invoca e o que executa a um comando

from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    """all commands will implement this interface"""
    @staticmethod
    @abstractmethod
    def execute():
        """required object all objects wil use"""

class Invoker():
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        """register commands in the invoker"""
        self._commands[command_name] = command

    def execute(self, command_name):
        """execute any registered command"""
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f'command {command_name} not recognised')

class Receiver():
    @staticmethod
    def run_command_1():
        print('executing command 1')
    @staticmethod
    def run_command_2():
        print('executing command 2')

class Command1(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_1()

class Command2(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.run_command_2()

RECEIVER = Receiver()

COMMAND_1 = Command1(RECEIVER)
COMMAND_2 = Command2(RECEIVER)

INVOKER = Invoker()
INVOKER.register('1', COMMAND_1)
INVOKER.register('2', COMMAND_2)

INVOKER.execute('1')
INVOKER.execute('2')
