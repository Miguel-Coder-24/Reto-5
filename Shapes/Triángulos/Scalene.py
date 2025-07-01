from .triangle import Triangle

class Scalene(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(False)
        lengths = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if (abs(lengths[0] - lengths[1]) < tolerance or
            abs(lengths[1] - lengths[2]) < tolerance or
            abs(lengths[2] - lengths[0]) < tolerance):
            print("Advertencia: Este triángulo no es escaleno (tiene lados iguales).")