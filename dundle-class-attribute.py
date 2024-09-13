# a classe de um objeto pode ser alterada usando self.__class__ = otherclass
# fazer isso nao afeta nenhum atributo criado durante a inicializacao (__init__) ja que o objeto em si nao foi alterado
# apenas as referencias aos metodos e atributos estaticos substituidos com o da nova class
# nao afeta nenhum atributo da instancia (self)

class ClassA():
    static_attribute = 'a'

    def __init__(self):
        self.instance_attribute = 'a'

    def instance_method(self):
        print('instance method a')

    @staticmethod
    def static_method():
        print('static method a')

    @classmethod
    def class_method(cls):
        print('class method a')


class ClassB():
    static_attribute = 'b'

    def __init__(self):
        self.instance_attribute = 'a'

    def instance_method(self):
        print('instance method b')

    @staticmethod
    def static_method():
        print('static method b')

    @classmethod
    def class_method(cls):
        print('class method b')


OBJ_A = ClassA()
print(id(OBJ_A))
print(f'static attribute {OBJ_A.static_attribute}')
print(f'instance attribute {OBJ_A.instance_attribute}')
OBJ_A.static_method()
OBJ_A.instance_method()
OBJ_A.class_method()

print('\n\n', end='')

OBJ_A.__class__ = ClassB
print(id(OBJ_A))
print(f'static attribute {OBJ_A.static_attribute}')
print(f'instance attribute {OBJ_A.instance_attribute}')
OBJ_A.static_method()
OBJ_A.instance_method()
OBJ_A.class_method()
