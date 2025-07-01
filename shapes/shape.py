from .point import Point
from .line import Line

class Shape:
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        # Se usan listas vacías si no se proporcionan
        self._vertices = vertices if vertices is not None else []
        self._edges = edges if edges is not None else []
        self._inner_angles = inner_angles if inner_angles is not None else []
        self._is_regular = is_regular

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        if isinstance(vertices, list) and all(isinstance(v, Point) for v in vertices):
            self._vertices = vertices
        else:
            print("Error: vertices debe ser una lista de objetos Point.")

    def get_edges(self):
        return self._edges

    def set_edges(self, edges):
        if isinstance(edges, list) and all(isinstance(e, Line) for e in edges):
            self._edges = edges
        else:
            print("Error: edges debe ser una lista de objetos Line.")

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, angles):
        if isinstance(angles, list) and all(isinstance(a, (int, float)) for a in angles):
            self._inner_angles = angles
        else:
            print("Error: inner_angles debe ser una lista de números.")

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, is_regular):
        if isinstance(is_regular, bool):
            self._is_regular = is_regular
        else:
            print("Error: is_regular debe ser booleano.")

    def compute_area(self):
        print("compute_area no implementado para Shape base.")
        return None

    def compute_perimeter(self):
        print("compute_perimeter no implementado para Shape base.")
        return None

    def compute_inner_angles(self):
        print("compute_inner_angles no implementado para Shape base.")
        return None