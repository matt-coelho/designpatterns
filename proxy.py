# a class functioning as an interface to another class or object
from abc import ABCMeta, abstractmethod

class ISubject(metaclass=ABCMeta):
    """interface implemented by the proxy and the real object"""
    @staticmethod
    @abstractmethod
    def request():
        """method to implement"""

class RealSubject(ISubject):
    """the object the proxy will represent"""
    def __init__(self):
        # hypothetical enormous amount of data
        self.enormous_data = [1,2,3,4,5,6,7,8,9,10]
    def request(self):
        return self.enormous_data

class Proxy(ISubject):
    """in this case the proxy will act as cache and only populates enormous_data when necessary"""
    def __init__(self):
        self.enormous_data = []
        self.real_subject = RealSubject()
    def request(self):
        """only adds data to the cache when needed"""
        if self.enormous_data == []:
            print('pulling data from realsubject')
            self.enormous_data = self.real_subject.request()
            return self.enormous_data
        print('pulling data from cache')
        return self.enormous_data

SUBJECT = Proxy()
print(id(SUBJECT))

print(SUBJECT.request())
print(SUBJECT.request())
