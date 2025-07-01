from .point import Point
import math

class Line:
    def __init__(self, start=None, end=None):
        # Si no se proporcionan puntos, inicializamos en (0,0)
        if start is None:
            start = Point()
        if end is None:
            end = Point()
        self._start = start
        self._end = end
        self._length = self.compute_length()
        self._slope = self.compute_slope()

    def get_start(self):
        return self._start

    def set_start(self, start):
        if isinstance(start, Point):
            self._start = start
            self._length = self.compute_length()
            self._slope = self.compute_slope()
        else:
            print("Error: El punto de inicio debe ser un objeto Point.")

    def get_end(self):
        return self._end

    def set_end(self, end):
        if isinstance(end, Point):
            self._end = end
            self._length = self.compute_length()
            self._slope = self.compute_slope()
        else:
            print("Error: El punto final debe ser un objeto Point.")

    def get_length(self):
        return self._length

    def get_slope(self):
        return self._slope

    # Método para calcular longitud usando distancia euclidiana
    def compute_length(self):
        dx = self._end.get_x() - self._start.get_x()
        dy = self._end.get_y() - self._start.get_y()
        length = math.sqrt(dx**2 + dy**2)
        return length

    # Método para calcular pendiente en grados
    def compute_slope(self):
        dx = self._end.get_x() - self._start.get_x()
        dy = self._end.get_y() - self._start.get_y()
        # Prevenir división por cero y casos verticales
        if dx == 0:
            slope_deg = 90.0 if dy > 0 else -90.0
        else:
            slope_rad = math.atan2(dy, dx)
            slope_deg = math.degrees(slope_rad)
        return slope_deg

    def __repr__(self):
        return f"Line(Start={self._start}, End={self._end})"
