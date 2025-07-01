# Reto 5: 
1. Create a package with all code of class *Shape*, this exersice should be conducted in two ways:
 - A unique module inside of package *Shape*
 - Individual modules that import *Shape* in inheritates from it.

Este proyecto implementa un paquete Python llamado `Shapes`, el cual contiene clases geométricas orientadas a objetos para representar y trabajar con figuras como puntos, líneas, triángulos, rectángulos y cuadrados.

---

##  Estructura del paquete

```plaintext
Shapes/
│
├── baseclass/
│   ├── point.py         # Clase Point (coordenadas x, y)
│   ├── line.py          # Clase Line (segmento entre dos Point)
│   ├── shape.py         # Clase base abstracta Shape
│   └── __init__.py
│
├── Rectángulos/
│   ├── Rectangle.py     # Clase Rectangle (hereda de Shape)
│   ├── Square.py        # Clase Square (hereda de Rectangle)
│   └── __init__.py
│
├── Triángulos/
│   ├── triangle.py      # Clase base Triangle (hereda de Shape)
│   ├── Isosceles.py     # Clase Isosceles (hereda de Triangle)
│   ├── Equilateral.py   # Clase Equilateral (hereda de Triangle)
│   ├── Scalene.py       # Clase Scalene (hereda de Triangle)
│   ├── TriRectangle.py  # Clase TriRectangle (hereda de Triangle)
│   └── __init__.py
│
└── __init__.py          # Importaciones globales del paquete
