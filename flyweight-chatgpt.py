class FlyweightFactory:
    def __init__(self):
        # Dicionário para armazenar as instâncias flyweight
        self.flyweights = {}

    def get_flyweight(self, char):
        # Verifica se a letra já existe, se não, cria uma nova
        if char not in self.flyweights:
            self.flyweights[char] = Flyweight(char)
        return self.flyweights[char]

class Flyweight:
    def __init__(self, char):
        self.char = char

    def display(self, position):
        # Exibe a letra e sua posição no texto
        return f"Caractere '{self.char}' na posição {position}"

class Document:
    def __init__(self, factory, text):
        # Armazena letras com suas respectivas posições
        self.letters_with_positions = [(factory.get_flyweight(char), pos) for pos, char in enumerate(text)]

    def display(self):
        # Mostra o texto inteiro com as posições
        for letter, position in self.letters_with_positions:
            print(letter.display(position))

# Exemplo de uso
factory = FlyweightFactory()
document = Document(factory, "banana")

document.display()

# Verificando o armazenamento
print("\nLetras únicas armazenadas:", list(factory.flyweights.keys()))
