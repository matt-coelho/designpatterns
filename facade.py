# simplified api over one or more complex systems
# reduced or simplified interface to a set of other interfaces, abstractions and implementations

class SubSystemA:
    @staticmethod
    def method():
        return 'A'
class SubSystemB:
    @staticmethod
    def method(value):
        return value
class SubSystemC:
    @staticmethod
    def method(value):
        return value
class Facade:
    @staticmethod
    def subsystem_a():
        return SubSystemA().method()
    @staticmethod
    def subsystem_b(value):
        return SubSystemB().method(value)
    @staticmethod
    def subsystem_c(value):
        return SubSystemC().method(value)

# print(SubSystemA.method())
# print(SubSystemB.method("b"))
# print(SubSystemC.method({"c":[1,2,3]}))

print(Facade.subsystem_a())
print(Facade.subsystem_b("b"))
print(Facade.subsystem_c({"c":[1,2,3]}))