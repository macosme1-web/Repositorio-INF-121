import math

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # Magnitud del vector
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Producto punto
    def __mul__(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    # Producto cruz
    def __xor__(self, otro):
        return Vector(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )

    # Escalar por vector
    def __rmul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar, self.z * escalar)

    # Resta de vectores
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    # Suma de vectores
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)


class AlgebraVectorial:
    @staticmethod
    def son_perpendiculares(a, b):
        return (a * b) == 0

    @staticmethod
    def son_paralelos(a, b):
        return (a ^ b).magnitud() == 0

    @staticmethod
    def proyeccion_de_a_sobre_b(a, b):
        escalar = (a * b) / (b.magnitud()**2)
        return escalar * b

    @staticmethod
    def componente_de_a_en_b(a, b):
        return (a * b) / b.magnitud()


# ------------------ PRUEBA ------------------
if __name__ == "__main__":
    a = Vector(2, 3, 0)
    b = Vector(-3, 2, 0)

    print("Vector a:", a)
    print("Vector b:", b)

    print("¿Son perpendiculares?", AlgebraVectorial.son_perpendiculares(a, b))
    print("¿Son paralelos?", AlgebraVectorial.son_paralelos(a, b))

    proy = AlgebraVectorial.proyeccion_de_a_sobre_b(a, b)
    print("Proyección de a sobre b:", proy)

    comp = AlgebraVectorial.componente_de_a_en_b(a, b)
    print("Componente de a en dirección de b:", comp)
