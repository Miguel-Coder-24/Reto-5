from .Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(True)
        # Valida que todos los lados sean iguales
        sides = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if not all(abs(sides[0] - s) < tolerance for s in sides[1:]):
            print("Advertencia: Este cuadrado no tiene todos los lados iguales.")