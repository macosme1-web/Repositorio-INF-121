import math
from typing import Tuple

class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    # Suma
    def __add__(self, otro: "Vector") -> "Vector":
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    # Resta
    def __sub__(self, otro: "Vector") -> "Vector":
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    # Multiplicación por escalar: a * r
    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            return Vector(self.x * otro, self.y * otro, self.z * otro)
        raise TypeError("Multiplicación sólo soporta scalars. Para producto punto use @")

    # Escalar * Vector  (soporta r * a)
    def __rmul__(self, escalar):
        return self.__mul__(escalar)

    # Producto punto usando el operador @ (matmul)
    def __matmul__(self, otro: "Vector") -> float:
        return self.x * otro.x + self.y * otro.y + self.z * otro.z

    # Producto cruz usando ^
    def __xor__(self, otro: "Vector") -> "Vector":
        cx = self.y * otro.z - self.z * otro.y
        cy = self.z * otro.x - self.x * otro.z
        cz = self.x * otro.y - self.y * otro.x
        return Vector(cx, cy, cz)

    # Magnitud (longitud)
    def magnitud(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Normal (vector unitario)
    def normal(self) -> "Vector":
        mag = self.magnitud()
        if mag == 0:
            raise ValueError("No se puede normalizar el vector cero")
        return Vector(self.x / mag, self.y / mag, self.z / mag)

    # Método auxiliar para comprobar si es vector nulo
    def es_cero(self) -> bool:
        return self.x == 0 and self.y == 0 and self.z == 0


class AlgebraVectorial:
    """Clase con métodos estáticos que implementan las operaciones del enunciado."""

    @staticmethod
    def suma(a: Vector, b: Vector) -> Vector:
        return a + b

    @staticmethod
    def multiplicacion_escalar(r: float, a: Vector) -> Vector:
        return r * a

    @staticmethod
    def longitud(a: Vector) -> float:
        return a.magnitud()

    @staticmethod
    def normal(a: Vector) -> Vector:
        return a.normal()

    @staticmethod
    def producto_escalar(a: Vector, b: Vector) -> float:
        return a @ b

    @staticmethod
    def producto_vectorial(a: Vector, b: Vector) -> Vector:
        return a ^ b

    # Métodos de comprobación (útiles para ejercicios)
    @staticmethod
    def son_perpendiculares(a: Vector, b: Vector) -> bool:
        return math.isclose(a @ b, 0.0, abs_tol=1e-9)

    @staticmethod
    def son_paralelos(a: Vector, b: Vector) -> bool:
        # paralelos si su producto cruz es vector cero
        return (a ^ b).es_cero()

    @staticmethod
    def proyeccion_de_a_sobre_b(a: Vector, b: Vector) -> Vector:
        if b.es_cero():
            raise ValueError("No se puede proyectar sobre el vector cero")
        escalar = (a @ b) / (b.magnitud() ** 2)
        return escalar * b

    @staticmethod
    def componente_de_a_en_b(a: Vector, b: Vector) -> float:
        if b.es_cero():
            raise ValueError("Componente indefinida sobre el vector cero")
        return (a @ b) / b.magnitud()


# ------------------ EJEMPLOS / PRUEBA ------------------
if __name__ == "__main__":
    a = Vector(4, -1, 2)
    b = Vector(1, 2, -2)

    print("a =", a)
    print("b =", b)

    print("Suma a + b =", AlgebraVectorial.suma(a, b))
    print("Multiplicar 3 * a =", AlgebraVectorial.multiplicacion_escalar(3, a))
    print("|a| =", AlgebraVectorial.longitud(a))
    print("Normal de a =", AlgebraVectorial.normal(a))
    print("Producto escalar a·b =", AlgebraVectorial.producto_escalar(a, b))
    print("Producto vectorial a×b =", AlgebraVectorial.producto_vectorial(a, b))

    print("¿Perpendiculares?", AlgebraVectorial.son_perpendiculares(a, b))
    print("¿Paralelos?", AlgebraVectorial.son_paralelos(a, b))

    print("Proyección de a sobre b =", AlgebraVectorial.proyeccion_de_a_sobre_b(a, b))
    print("Componente de a en b =", AlgebraVectorial.componente_de_a_en_b(a, b))
