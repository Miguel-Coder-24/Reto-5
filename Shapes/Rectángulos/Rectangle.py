from ..baseclass.point import Point
from ..baseclass.line import Line
from ..baseclass.shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices=vertices, edges=edges)
        self.set_is_regular(True)

        # Si vertices son dados, construimos las aristas
        if vertices and len(vertices) == 4:
            self._edges = [
                Line(vertices[0], vertices[1]),
                Line(vertices[1], vertices[2]),
                Line(vertices[2], vertices[3]),
                Line(vertices[3], vertices[0])
            ]
        elif edges and len(edges) == 4:
            self._vertices = [
                edges[0].get_start(),
                edges[0].get_end(),
                edges[1].get_end(),
                edges[2].get_end()
            ]
        else:
            print("Error: Un rectángulo debe tener 4 vértices o 4 aristas.")

        # Se asumen lados opuestos iguales
        self._width = self._edges[0].get_length()
        self._height = self._edges[1].get_length()

    def compute_area(self):
        return self._width * self._height

    def compute_perimeter(self):
        return 2 * (self._width + self._height)

    def compute_inner_angles(self):
        self._inner_angles = [90, 90, 90, 90]
        return self._inner_angles
