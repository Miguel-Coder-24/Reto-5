class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self._x = x
        else:
            print("Error: La coordenada x debe ser numérica.")

    def get_y(self):
        return self._y

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self._y = y
        else:
            print("Error: La coordenada y debe ser numérica.")

    def __repr__(self):
        return f"Point({self._x}, {self._y})"
