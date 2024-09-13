"""
capaz de salvar uma copia do estado atual do sistema para recuperacao posterior
é tambem comumente usado para acoes de refazer/desfazer, mas ao inves de reexecutar comandos em uma ordem,
substituir completamente o estado atual pelo que esta salvo em cache/store
"""

class Memento():
    def __init__(self, state):
        self.state = state

class Originator():
    """object whose the state changes"""
    def __init__(self):
        self._state = ''

    @property
    def state(self):
        """get for object state"""
        return self._state

    @state.setter
    def state(self, state):
        print(f'originator setting state to {state}')
        self._state = state
    
    @property
    def memento(self):
        print('originator providing memento of state to caretaker')
        return Memento(self._state)

    @memento.setter
    def memento(self, memento):
        self._state = memento.state
        print(f'originator state after restoring from memento {self._state}')

class Caretaker():
    """provides a narrow interface to the mementos"""
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def create(self):
        """store a new memento of the originators current state"""
        print('caretaker getting a copy of originators current state')
        memento = self._originator.memento
        self._mementos.append(memento)

    def restore(self, index):
        """replaces the originator current state with the state stored in the saved memento"""
        print(f'caretaker restoring originators state from memento')
        memento = self._mementos[index]
        self._originator.memento = memento

ORIGINATOR = Originator()
CARETAKER = Caretaker(ORIGINATOR)

ORIGINATOR.state = 'st1'
ORIGINATOR.state = 'st2'

# backups the original states
CARETAKER.create()

ORIGINATOR.state = 'st3'
CARETAKER.create()

ORIGINATOR.state = 'st4'
print(ORIGINATOR.state)

CARETAKER.restore(0)
print(ORIGINATOR.state)

CARETAKER.restore(1)
print(ORIGINATOR.state)
