from .triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(False)
        self.compute_inner_angles()
        if 90 not in [round(angle) for angle in self._inner_angles]:
            print("Advertencia: Este triángulo no es rectángulo (no tiene un ángulo de 90 grados).")