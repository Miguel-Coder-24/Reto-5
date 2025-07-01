from ..baseclass.point import Point
from ..baseclass.line import Line
from ..baseclass.shape import Shape

class Triangle(Shape):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices=vertices, edges=edges)
        if vertices and len(vertices) == 3:
            self._edges = [
                Line(vertices[0], vertices[1]),
                Line(vertices[1], vertices[2]),
                Line(vertices[2], vertices[0])
            ]
        elif edges and len(edges) == 3:
            self._vertices = [
                edges[0].get_start(),
                edges[0].get_end(),
                edges[1].get_end()
            ]
        else:
            print("Error: Un triángulo debe tener 3 vértices o 3 aristas.")

    def compute_area(self):
        # Fórmula de Herón
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        s = (a + b + c) / 2
        try:
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        except ValueError:
            print("Error: No es un triángulo válido para cálculo de área.")
            return 0

    def compute_perimeter(self):
        perimeter = sum(edge.get_length() for edge in self._edges)
        return perimeter

    def compute_inner_angles(self):
        # Calculamos usando la ley de cosenos
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        try:
            angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
            angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
            angle_C = 180 - angle_A - angle_B
            self._inner_angles = [angle_A, angle_B, angle_C]
            return self._inner_angles
        except ValueError:
            print("Error: Ángulos no válidos para triángulo.")
            return []