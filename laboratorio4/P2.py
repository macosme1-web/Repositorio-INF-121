from abc import ABC, abstractmethod
import random
import math

# Interfaz Coloreado
class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self) -> str:
        pass

# Clase abstracta Figura
class Figura(ABC):
    def __init__(self, color: str):
        self.color = color

    def set_color(self, color: str):
        self.color = color

    def get_color(self) -> str:
        return self.color

    def __str__(self) -> str:
        return f"Figura de color {self.color}"

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

# Clase Cuadrado que implementa Coloreado
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado: float, color: str):
        super().__init__(color)
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado

    def como_colorear(self) -> str:
        return "Colorear los cuatro lados"

    def __str__(self) -> str:
        return f"Cuadrado(color={self.color}, lado={self.lado})"

# Clase Circulo
class Circulo(Figura):
    def __init__(self, radio: float, color: str):
        super().__init__(color)
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def __str__(self) -> str:
        return f"Circulo(color={self.color}, radio={self.radio})"

# Crear lista de figuras aleatorias
def crear_figuras():
    figuras = []
    colores = ['rojo', 'azul', 'verde', 'amarillo', 'negro']

    for _ in range(5):
        tipo = random.randint(1, 2)  # 1 para Cuadrado, 2 para Circulo
        color = random.choice(colores)

        if tipo == 1:
            lado = round(random.uniform(1.0, 10.0), 2)
            figura = Cuadrado(lado, color)
        else:
            radio = round(random.uniform(1.0, 10.0), 2)
            figura = Circulo(radio, color)

        figuras.append(figura)
    
    return figuras

# Mostrar la información de cada figura
def mostrar_info_figuras(figuras):
    for figura in figuras:
        print(figura)
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")

        if isinstance(figura, Coloreado):
            print("Coloración:", figura.como_colorear())
        print('-' * 40)

# Programa principal
if __name__ == "__main__":
    figuras = crear_figuras()
    mostrar_info_figuras(figuras)
