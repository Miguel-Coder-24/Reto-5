from .triangle import Triangle

class Isosceles(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(False)
        # Validamos lados iguales
        lengths = [edge.get_length() for edge in self._edges]
        # Comprobamos si al menos dos lados son iguales (dentro de tolerancia)
        tolerance = 1e-6
        sides_equal = (
            abs(lengths[0] - lengths[1]) < tolerance or
            abs(lengths[1] - lengths[2]) < tolerance or
            abs(lengths[2] - lengths[0]) < tolerance
        )
        if not sides_equal:
            print("Advertencia: Este triángulo no cumple la condición de isósceles.")