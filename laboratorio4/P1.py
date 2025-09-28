from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario_mensual(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre}"

# Subclase EmpleadoTiempoCompleto
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_anual):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self):
        return self.salario_anual / 12

    def __str__(self):
        return (super().__str__() +
                f", Salario Anual: ${self.salario_anual:.2f}, " +
                f"Salario Mensual: ${self.calcular_salario_mensual():.2f}")

# Subclase EmpleadoTiempoHorario
class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario_mensual(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def __str__(self):
        return (super().__str__() +
                f", Horas Trabajadas: {self.horas_trabajadas}, " +
                f"Tarifa por Hora: ${self.tarifa_por_hora:.2f}, " +
                f"Salario Mensual: ${self.calcular_salario_mensual():.2f}")

# Programa principal
def main():
    empleados = []

    # Ingresar 2 empleados a tiempo completo
    for i in range(2):
        print(f"\nEmpleado a Tiempo Completo #{i + 1}")
        nombre = input("Nombre: ")
        salario_anual = float(input("Salario anual: "))
        empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))

    # Ingresar 3 empleados por horas
    for i in range(3):
        print(f"\nEmpleado por Horas #{i + 1}")
        nombre = input("Nombre: ")
        horas = float(input("Horas trabajadas: "))
        tarifa = float(input("Tarifa por hora: "))
        empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

    # Mostrar la información de todos los empleados
    print("\n--- Lista de Empleados ---")
    for emp in empleados:
        print(emp)

if __name__ == "__main__":
    main()
