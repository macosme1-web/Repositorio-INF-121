import json
import os
from datetime import date
import tkinter as tk
from tkinter import messagebox, simpledialog

class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido


class Libro:
    def __init__(self, titulo, isbn, paginas_info):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(n, c) for n, c in paginas_info]

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "isbn": self.isbn,
            "paginas": [(p.numero, p.contenido) for p in self.paginas]
        }


class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }


class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def to_dict(self):
        return {"codigo": self.codigo, "nombre": self.nombre}


class Prestamo:
    def __init__(self, estudiante, libro):
        self.fecha_prestamo = str(date.today())
        self.fecha_devolucion = None
        self.estudiante = estudiante
        self.libro = libro

    def to_dict(self):
        return {
            "estudiante": self.estudiante.codigo,
            "libro": self.libro.isbn,
            "fecha": self.fecha_prestamo
        }


class Horario:
    def __init__(self, dias, hora_apertura, hora_cierre):
        self.dias = dias
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre


class Biblioteca:
    def __init__(self, nombre, dias, hora_apertura, hora_cierre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.estudiantes = []
        self.prestamos = []
        self.horario = Horario(dias, hora_apertura, hora_cierre)

        self.archivo = "biblioteca.json"
        self.cargar()

    # -------------------- Persistencia --------------------
    def guardar(self):
        data = {
            "libros": [l.to_dict() for l in self.libros],
            "autores": [a.to_dict() for a in self.autores],
            "estudiantes": [e.to_dict() for e in self.estudiantes],
            "prestamos": [p.to_dict() for p in self.prestamos]
        }

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print("Datos guardados.")

    def cargar(self):
        if not os.path.exists(self.archivo):
            return

        with open(self.archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Cargar autores
        for a in data["autores"]:
            self.autores.append(Autor(a["nombre"], a["nacionalidad"]))

        # Cargar estudiantes
        for e in data["estudiantes"]:
            self.estudiantes.append(Estudiante(e["codigo"], e["nombre"]))

        # Cargar libros
        for l in data["libros"]:
            self.libros.append(Libro(l["titulo"], l["isbn"], l["paginas"]))

        # Cargar préstamos
        for p in data["prestamos"]:
            est = self.buscarEstudiante(p["estudiante"])
            lib = self.buscarLibro(p["libro"])
            if est and lib:
                self.prestamos.append(Prestamo(est, lib))

        print("Datos cargados correctamente.")

    # -----------------------------------------------------

    def agregarLibro(self, libro):
        self.libros.append(libro)
        self.guardar()

    def agregarAutor(self, autor):
        self.autores.append(autor)
        self.guardar()

    def agregarEstudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        self.guardar()

    def buscarEstudiante(self, codigo):
        return next((e for e in self.estudiantes if e.codigo == codigo), None)

    def buscarLibro(self, isbn):
        return next((l for l in self.libros if l.isbn == isbn), None)

    def prestarLibro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        self.guardar()

    def mostrarEstadoTexto(self):
        return (
            f"Biblioteca: {self.nombre}\n"
            f"Libros: {[l.titulo for l in self.libros]}\n"
            f"Autores: {[a.nombre for a in self.autores]}\n"
            f"Estudiantes: {[e.nombre for e in self.estudiantes]}\n"
            f"Préstamos activos: {len(self.prestamos)}"
        )


# =====================================================
#                INTERFAZ GRÁFICA TKINTER
# =====================================================

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca UMSA")

        self.biblio = Biblioteca("UMSA", "Lunes a Viernes", "08:00", "18:00")

        tk.Button(root, text="Agregar Autor", command=self.agregarAutor).pack(pady=5)
        tk.Button(root, text="Agregar Libro", command=self.agregarLibro).pack(pady=5)
        tk.Button(root, text="Agregar Estudiante", command=self.agregarEstudiante).pack(pady=5)
        tk.Button(root, text="Prestar Libro", command=self.prestarLibro).pack(pady=5)
        tk.Button(root, text="Mostrar Estado", command=self.mostrarEstado).pack(pady=5)

    def agregarAutor(self):
        nombre = simpledialog.askstring("Autor", "Nombre:")
        nac = simpledialog.askstring("Autor", "Nacionalidad:")
        if nombre and nac:
            self.biblio.agregarAutor(Autor(nombre, nac))
            messagebox.showinfo("OK", "Autor agregado exitosamente.")

    def agregarLibro(self):
        titulo = simpledialog.askstring("Libro", "Título:")
        isbn = simpledialog.askstring("Libro", "ISBN:")
        paginas = [(1, "Página inicial")]
        if titulo and isbn:
            self.biblio.agregarLibro(Libro(titulo, isbn, paginas))
            messagebox.showinfo("OK", "Libro agregado exitosamente.")

    def agregarEstudiante(self):
        codigo = simpledialog.askstring("Estudiante", "Código:")
        nombre = simpledialog.askstring("Estudiante", "Nombre:")
        if codigo and nombre:
            self.biblio.agregarEstudiante(Estudiante(codigo, nombre))
            messagebox.showinfo("OK", "Estudiante agregado.")

    def prestarLibro(self):
        cod = simpledialog.askstring("Préstamo", "Código estudiante:")
        isbn = simpledialog.askstring("Préstamo", "ISBN libro:")

        est = self.biblio.buscarEstudiante(cod)
        lib = self.biblio.buscarLibro(isbn)

        if not est:
            messagebox.showerror("Error", "Estudiante no encontrado.")
            return
        if not lib:
            messagebox.showerror("Error", "Libro no encontrado.")
            return

        self.biblio.prestarLibro(est, lib)
        messagebox.showinfo("OK", "Préstamo realizado.")

    def mostrarEstado(self):
        messagebox.showinfo("Estado", self.biblio.mostrarEstadoTexto())

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
