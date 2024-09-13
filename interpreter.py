# helps convert information from one language into another

class AbstractExpression():
    """all terminal and non-terminal expressions will implement an interpret method"""
    @staticmethod
    def interpret():
        """gets called recursively for each abstractexpression"""

class Number(AbstractExpression):
    """terminal expression"""
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class Add(AbstractExpression):
    """non-terminal expression"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} add {self.right})"

class Subtract(AbstractExpression):
    """Non-terminal expression"""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} subtract {self.right})"

SENTENCE = "5 + 4 - 3 + 7 - 2"

TOKENS = SENTENCE.split(" ")
print(TOKENS)

AST: list[AbstractExpression] = [] # python 3.9+
# AST = [] # python 3.8-
AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))
AST.append(Subtract(AST[0], Number(TOKENS[4])))
AST.append(Add(AST[1], Number(TOKENS[6])))
AST.append(Subtract(AST[2], Number(TOKENS[8])))

AST_ROOT = AST.pop()
print(AST_ROOT.interpret())

print(AST_ROOT)
