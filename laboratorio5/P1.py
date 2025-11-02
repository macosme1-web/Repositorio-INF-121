# Sistema de Biblioteca Universitaria
# Implementa composición, agregación y asociación según el enunciado.

from datetime import date

# ------------------------------
# Clase Pagina (Composición con Libro)
# ------------------------------
class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrarPagina(self):
        print(f"Página {self.numero}: {self.contenido}")


# ------------------------------
# Clase Libro (Agregación con Biblioteca, Composición con Pagina)
# ------------------------------
class Libro:
    def __init__(self, titulo, isbn, paginas_info):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(num, cont) for num, cont in paginas_info]  # composición

    def leer(self):
        print(f"Leyendo '{self.titulo}':")
        for pagina in self.paginas:
            pagina.mostrarPagina()


# ------------------------------
# Clase Autor (Agregación con Biblioteca)
# ------------------------------
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarInfo(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")


# ------------------------------
# Clase Estudiante (Asociación con Prestamo)
# ------------------------------
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrarInfo(self):
        print(f"Estudiante: {self.nombre} (Código {self.codigo})")


# ------------------------------
# Clase Prestamo (Asociación entre Estudiante y Libro)
# ------------------------------
class Prestamo:
    def __init__(self, estudiante, libro):
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.estudiante = estudiante
        self.libro = libro

    def mostrarInfo(self):
        print(f"Préstamo del libro '{self.libro.titulo}' a {self.estudiante.nombre} el {self.fecha_prestamo}")


# ------------------------------
# Clase Horario (Composición con Biblioteca)
# ------------------------------
class Horario:
    def __init__(self, dias, hora_apertura, hora_cierre):
        self.dias = dias
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrarHorario(self):
        print(f"Horario: {self.dias}, {self.hora_apertura} - {self.hora_cierre}")


# ------------------------------
# Clase Biblioteca (Agregación con Libro y Autor, Composición con Horario)
# ------------------------------
class Biblioteca:
    def __init__(self, nombre, dias, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.libros = []  # agregación
        self.autores = []  # agregación
        self.prestamos = []
        self.horario = Horario(dias, hora_apertura, hora_cierre)  # composición

    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarAutor(self, autor):
        self.autores.append(autor)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f"Libro '{libro.titulo}' prestado a {estudiante.nombre}.")

    def mostrarEstado(self):
        print(f"===== Biblioteca {self.nombre} =====")
        self.horario.mostrarHorario()
        print(f"Libros disponibles: {[l.titulo for l in self.libros]}")
        print(f"Autores registrados: {[a.nombre for a in self.autores]}")
        print(f"Préstamos activos: {len(self.prestamos)}")

    def cerrarBiblioteca(self):
        print(f"Cerrando la biblioteca {self.nombre}... Todos los préstamos finalizan.")
        self.prestamos.clear()


# ------------------------------
# PRUEBA DEL SISTEMA
# ------------------------------
if __name__ == "__main__":

    autor1 = Autor("Gabriel García Márquez", "Colombiano")
    autor2 = Autor("Isabel Allende", "Chilena")

    paginas_libro1 = [(1, "Era un día soleado..."), (2, "El viento soplaba con fuerza.")]
    libro1 = Libro("Cien años de soledad", "123456789", paginas_libro1)

    paginas_libro2 = [(1, "En el principio fue el verbo."), (2, "Y el verbo se hizo carne.")]
    libro2 = Libro("La casa de los espíritus", "987654321", paginas_libro2)


    biblioteca = Biblioteca("Biblioteca UMSA", "Lunes a Viernes", "08:00", "18:00")


    biblioteca.agregarLibro(libro1)
    biblioteca.agregarLibro(libro2)
    biblioteca.agregarAutor(autor1)
    biblioteca.agregarAutor(autor2)

    estudiante = Estudiante("202501", "Juan Pérez")
    biblioteca.prestarLibro(estudiante, libro1)
    
    biblioteca.mostrarEstado()

    
    libro1.leer()

   
    biblioteca.cerrarBiblioteca()
