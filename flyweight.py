# ao inves de criar varios objetos que compartilham atributos em comum, em uma situacao onde muitos recursos sao usados
# uma classe pode ser modificada para compartilhar varias instancias ao mesmo tempo usando uma referencia ao objeto compartilhado

class IFlyWeight():
    """nothing to implement"""

class Flyweight(IFlyWeight):
    """the concrete"""
    def __init__(self, code: str) -> None:
        self.code = code

class FlyweightFactory():
    """creating the factory as singleton"""
    _flyweights: dict[str, Flyweight] = {}

    def __new__(cls):
        return cls

    @classmethod
    def get_flyweight(cls, code: str) -> Flyweight:
        """static method to get a flyweight based on a code"""
        if not code in cls._flyweights:
            cls._flyweights[code] = Flyweight(code)
        return cls._flyweights[code]

    @classmethod
    def get_count(cls) -> int:
        return len(cls._flyweights)

class Context():
    def __init__(self, codes: str)->None:
        self.codes = list(codes)

    def output(self):
        ret = ""
        for code in self.codes:
            ret = ret + FlyweightFactory.get_flyweight(code).code
        return ret


word = "abracadabra"
CONTEXT = Context(word)
print(CONTEXT.output())

print(f"{word} has {len(word)} letters")
print(f"flyweightfactory has {FlyweightFactory.get_count()} flyweights")

print(CONTEXT.codes)
print(FlyweightFactory._flyweights)
