import pickle
from pathlib import Path

# Creación de la Clase Libro
class Libro:

    # Método Constructor
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    # Método agregar la clase Libro a la lista biblioteca
    def agregar(self, biblioteca):
        biblioteca.append(self)
        print(f"Libro '{self.titulo}' agregado con éxito.")

    # Método prestar cambia el estado de disponible (False) prestado o presenta estado de disponible
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    # Método devolver cambia el estado de disponible (True) devuelto o presenta estado de disponible
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

# Función para mostrar todos los libros en la biblioteca
def mostrar(biblioteca):
    if not biblioteca:
        print("No hay libros en la biblioteca.")
    else:
        for libro in biblioteca:
            if libro.disponible:
                disponibilidad = "Sí"
            else:
                disponibilidad = "No"
            print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {disponibilidad}")

# Función para buscar un libro por ISBN
def buscar(biblioteca, isbn):
    for libro in biblioteca:
        if libro.isbn == isbn:
            if libro.disponible:
                disponibilidad = "Sí"
            else:
                disponibilidad = "No"
            print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {disponibilidad}")
            return
    print(f"No se encontró ningún libro con el ISBN {isbn}.")

# Función para mostrar el menú y recoger la opción
def menu():
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")
    return input("Elige una opción: ")

# Función principal del programa
def main():
    # Inicializa lista biblioteca
    biblioteca = []
    # Comprueba si existe el fichero y carga en lista biblioteca el contenido
    file_name = "biblioteca.pkl"
    path = Path(file_name)
    if path.is_file():
        input_file = open(file_name, 'rb')
        biblioteca = pickle.load(input_file)
        input_file.close()
    else:
        print("Fichero no existe, creamos nuevo")

    # Inicia bucle del menú mientras la opción sea distinta de "6"
    while True:
        opcion = menu()
        # Recoge atributos de clase Libro, instancia clase Libro y método agregar para añadir a lista biblioteca
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro_nuevo = Libro(titulo, autor, isbn)
            libro_nuevo.agregar(biblioteca)
        # Recoge atributo ISBN a prestar, recorre lista biblioteca al encontrar método prestar, sino presenta info
        elif opcion == "2":
            isbn = input("Ingresa el ISBN: ")
            libro_encontrado = False
            for libro in biblioteca:
                if libro.isbn == isbn:
                    libro.prestar()
                    libro_encontrado = True
                    break
            if not libro_encontrado:
                print(f"No se encontró ningún libro con el ISBN {isbn}.")
        # Recoge atributo ISBN a devolver, recorre lista biblioteca al encontrar método devolver, sino presenta info
        elif opcion == "3":
            isbn = input("Ingresa el ISBN: ")
            libro_encontrado = False
            for libro in biblioteca:
                if libro.isbn == isbn:
                    libro.devolver()
                    libro_encontrado = True
                    break
            if not libro_encontrado:
                print(f"No se encontró ningún libro con el ISBN {isbn}.")
        # Muestra todos los objetos libro de la lista biblioteca, con la función mostrar
        elif opcion == "4":
            mostrar(biblioteca)
        # Recoge atributo ISBN a buscar, si encuentra presenta objeto libro o presenta info
        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            buscar(biblioteca, isbn)
        # Opción de salir, guardando en fichero los objetos libro de la lista biblioteca
        elif opcion == "6":
            print("Salvando Biblioteca...")
            output_file = open(file_name, 'wb')
            pickle.dump(biblioteca, output_file)
            output_file.close()
            print("Saliendo del programa...")
            break
        # Presenta info de opción no válida
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

# Inicio del programa
if __name__ == "__main__":
    main()