import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numeroDeVidas = numero_de_vidas
        self.vidas_restantes = numero_de_vidas
        self.record = 0

    def reiniciaPartida(self):
        self.vidas_restantes = self.numeroDeVidas
        print(f"\nNueva partida iniciada con {self.numeroDeVidas} vidas.")

    def actualizaRecord(self):
        if self.vidas_restantes > self.record:
            self.record = self.vidas_restantes
            print(f"¡Nuevo récord! Vidas restantes: {self.vidas_restantes}")
        else:
            print(f"Récord actual: {self.record} vidas restantes")

    def quitaVida(self):
        self.vidas_restantes -= 1
        if self.vidas_restantes > 0:
            print(f"Te quedan {self.vidas_restantes} vidas.")
            return True
        else:
            print("Te has quedado sin vidas.")
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numero_de_vidas):
        super().__init__(numero_de_vidas)
        self.numeroAAdivinar = None

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        # print(f"[DEBUG] Número a adivinar: {self.numeroAAdivinar}")  # Descomenta para ver el número (debug)

        while True:
            try:
                intento = int(input("Adivina un número entre 0 y 10: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if intento == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print(f"El número correcto era: {self.numeroAAdivinar}")
                    break
                else:
                    pista = "mayor" if self.numeroAAdivinar > intento else "menor"
                    print(f" No acertaste. El número a adivinar es {pista} que {intento}. Intenta de nuevo.")

class Aplicacion:
    @staticmethod
    def main():
        print("=== Bienvenido al Juego de Adivinar el Número ===")
        vidas = 3  # Puedes cambiar la cantidad de vidas aquí
        juego = JuegoAdivinaNumero(vidas)
        juego.juega()

# Ejecutar el main si este archivo es el principal
if __name__ == "__main__":
    Aplicacion.main()
