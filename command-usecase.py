# smart light switch
# it will keep a history of each time its command was called

from abc import ABCMeta, abstractmethod
from datetime import datetime
import time

class ISwitch(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        """the required execute method all objects will use"""

class SwitchOff(ISwitch):
    def __init__(self, light):
        self._light = light
    def execute(self):
        self._light.turn_off()

class SwitchOn(ISwitch):
    def __init__(self, light):
        self._light = light
    def execute(self):
        self._light.turn_on()

class Switch():
    """the invoker class"""
    def __init__(self):
        self._commands = {}
        self._history = []

    def show_history(self):
        for row in self._history:
            print(f"{datetime.fromtimestamp(row[0]).strftime('%H:%M:%S')} {row[1]}")

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
            self._history.append((time.time(), command_name))
        else:
            print(f'command nao found {command_name}')

    def replay_last(self, number_of_commands):
        """replay last N commands"""
        commands = self._history[-number_of_commands:]
        for command in commands:
            self._commands[command[1]].execute()

class Light():
    """the receiver"""
    @staticmethod
    def turn_on():
        print('turned light on')

    @staticmethod
    def turn_off():
        print('turned light off')


LIGHT = Light()
SWITCH_ON = SwitchOn(LIGHT)
SWITCH_OFF = SwitchOff(LIGHT)

SWITCH = Switch()
SWITCH.register("ON", SWITCH_ON)
SWITCH.register('OFF', SWITCH_OFF)


SWITCH.execute('ON')
SWITCH.execute('OFF')
SWITCH.execute('ON')
SWITCH.execute('OFF')

SWITCH.show_history()
SWITCH.replay_last(2)
