class Persona:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

    
class Cabina:
    def __init__(self, nro_cabina, capacidad_maxima=10, peso_maximo=850):
        self.nro_cabina = nro_cabina
        self.capacidad_maxima = capacidad_maxima
        self.peso_maximo = peso_maximo
        self.personas_a_bordo = []
        self.peso_actual = 0

    def agregar_persona(self, persona):
        if len(self.personas_a_bordo) < self.capacidad_maxima and self.peso_actual + persona.peso <= self.peso_maximo:
            self.personas_a_bordo.append(persona)
            self.peso_actual += persona.peso
            return True
        else:
            print(f"No se puede agregar a {persona.nombre} en la cabina {self.nro_cabina}. Límite alcanzado.")
            return False

    def obtener_peso_total(self):
        return self.peso_actual

    def obtener_capacidad_actual(self):
        return len(self.personas_a_bordo)

    def mostrar_info(self):
        print(f"Cabina {self.nro_cabina} (Capacidad: {len(self.personas_a_bordo)} personas)")
        for persona in self.personas_a_bordo:
            print(f"  {persona}")


class Linea:
    def __init__(self, color):
        self.color = color
        self.cabinas = []
        self.ingresos_regulares = 0
        self.ingresos_menores = 0

    def agregar_cabina(self, cabina):
        self.cabinas.append(cabina)

    def agregar_ingreso(self, monto, es_menor=False):
        if es_menor:
            self.ingresos_menores += monto
        else:
            self.ingresos_regulares += monto

    def mostrar_info(self):
        print(f"Línea {self.color}:")
        for cabina in self.cabinas:
            cabina.mostrar_info()

    def obtener_ingreso_total(self):
        return self.ingresos_regulares + self.ingresos_menores


class MiTeleferico:
    def __init__(self):
        self.lineas = []

    def agregar_linea(self, linea):
        self.lineas.append(linea)

    def verificar_cumplimiento(self):
        for linea in self.lineas:
            for cabina in linea.cabinas:
                if cabina.obtener_capacidad_actual() > cabina.capacidad_maxima or cabina.obtener_peso_total() > cabina.peso_maximo:
                    print(f"Advertencia: La cabina {cabina.nro_cabina} de la línea {linea.color} no cumple con las reglas de abordo.")
                else:
                    print(f"La cabina {cabina.nro_cabina} de la línea {linea.color} cumple con las reglas de abordo.")

    def calcular_tarifas(self, persona):
        tarifa_regular = 3  
        if persona.edad < 18:
            tarifa_menor = tarifa_regular * 0.5  
            print(f"Tarifa para {persona.nombre} (Menor): {tarifa_menor} bs")
            return tarifa_menor, True
        else:
            print(f"Tarifa para {persona.nombre} (Regular): {tarifa_regular} bs")
            return tarifa_regular, False

    def mostrar_linea_mayor_ingreso(self):
        max_ingreso = 0
        linea_max_ingreso = None
        for linea in self.lineas:
            if linea.ingresos_regulares > max_ingreso:
                max_ingreso = linea.ingresos_regulares
                linea_max_ingreso = linea
        print(f"La línea con más ingresos de tarifa regular es la línea {linea_max_ingreso.color} con un total de {max_ingreso} bs.")



teleferico = MiTeleferico()


linea_roja = Linea("Roja")
linea_azul = Linea("Azul")


cabina1 = Cabina(1)
cabina2 = Cabina(2)

linea_roja.agregar_cabina(cabina1)
linea_azul.agregar_cabina(cabina2)


teleferico.agregar_linea(linea_roja)
teleferico.agregar_linea(linea_azul)


persona1 = Persona("Ana", 25, 60)
persona2 = Persona("Luis", 17, 50)
persona3 = Persona("Carlos", 18, 70)


cabina1.agregar_persona(persona1)
cabina1.agregar_persona(persona2)
cabina1.agregar_persona(persona3)


tarifa1, es_menor1 = teleferico.calcular_tarifas(persona1)
tarifa2, es_menor2 = teleferico.calcular_tarifas(persona2)
tarifa3, es_menor3 = teleferico.calcular_tarifas(persona3)


linea_roja.agregar_ingreso(tarifa1, es_menor1)
linea_roja.agregar_ingreso(tarifa2, es_menor2)
linea_azul.agregar_ingreso(tarifa3, es_menor3)


teleferico.verificar_cumplimiento()


teleferico.mostrar_linea_mayor_ingreso()
