from .triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(True)
        lengths = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if not (abs(lengths[0] - lengths[1]) < tolerance and abs(lengths[1] - lengths[2]) < tolerance):
            print("Advertencia: Este triángulo no es equilátero.")
