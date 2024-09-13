# Implementor (interface de renderização)
class Renderer:
    def render(self, shape):
        pass

# Concrete Implementor 1 (Renderização 2D)
class Renderer2D(Renderer):
    def render(self, shape):
        return f"Rendering {shape} in 2D"

# Concrete Implementor 2 (Renderização 3D)
class Renderer3D(Renderer):
    def render(self, shape):
        return f"Rendering {shape} in 3D"

# Abstraction (Forma geométrica)
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

# Refined Abstraction (Círculo)
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render(f"Circle with radius {self.radius}")

# Refined Abstraction (Quadrado)
class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        return self.renderer.render(f"Square with side {self.side}")

# Uso
renderer2d = Renderer2D()
renderer3d = Renderer3D()

circle2d = Circle(renderer2d, 5)
square3d = Square(renderer3d, 10)

print(circle2d.draw())  # "Rendering Circle with radius 5 in 2D"
print(square3d.draw())  # "Rendering Square with side 10 in 3D"