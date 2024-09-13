from abc import ABCMeta, abstractmethod

class IDataController(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """subscriber method to implement"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """unsubscribe method to implement"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """notify method to implement"""

class IDataModel(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """to implement"""
    @staticmethod
    @abstractmethod
    def unsubscribe(observer_id):
        """to implement"""
    @staticmethod
    @abstractmethod
    def notify(data):
        """to implement"""

class IDataView(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def notify(data):
        """receive notification to implement"""

    @staticmethod
    @abstractmethod
    def draw(data):
        """draw the view to implement"""

    @staticmethod
    @abstractmethod
    def delete():
        """remove observer specific resources to implement"""

class DataController(IDataController):
    _observers = set()

    def __new__(cls):
        return cls

    @classmethod
    def subscribe(cls, observer):
        cls._observers.add(observer)

    @classmethod
    def unsubscribe(cls, observer):
        cls._observers.remove(observer)

    @classmethod
    def notify(cls, *args):
        for observer in cls._observers:
            observer.notify(*args)

class DataModel(IDataModel):
    def __init__(self):
        self._observers = {}
        self._counter = 0
        self._data_controller = DataController()
        self._data_controller.subscribe(self)

    def subscribe(self, observer):
        self._counter = self._counter + 1
        self._observers[self._counter] = observer
        return self._counter

    def unsubscribe(self, observer_id):
        self._observers.pop(observer_id)

    def notify(self, data):
        for observer in self._observers:
            self._observers[observer].notify(data)

class PieDataView(IDataView):
    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f'pie graph id {self._id}')
        self.draw(data)

    def draw(self, data):
        print(f'drawing a pie graph using data {data}')

    def delete(self):
        self._observable.unsubscribe(self._id)

class BarGraphView(IDataView):
    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f'bar graph, id {self._id}')
        self.draw(data)

    def draw(self, data):
        print(f'drawing bar graph using data {data}')

    def delete(self):
        self._observable.unsubscribe(self._id)

class TableView(IDataView):
    def __init__(self, observable):
        self._observable = observable
        self._id = self._observable.subscribe(self)

    def notify(self, data):
        print(f'table view id {self._id}')
        self.draw(data)
    def draw(self, data):
        print(f'drawing table view {data}')
    def delete(self):
        self._observable.unsubscribe(self._id)

DATA_MODEL = DataModel()

PIE_GRAPH_VIEW = PieDataView(DATA_MODEL)
BAR_GRAPH_VIEW = BarGraphView(DATA_MODEL)
TABLE_VIEW = TableView(DATA_MODEL)

DATA_CONTROLLER = DataController()

DATA_CONTROLLER.notify([1,2,3])

BAR_GRAPH_VIEW.delete()

DATA_CONTROLLER.notify([4,5,6])