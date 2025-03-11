# Creacion de la Clase Libro
class Libro:
    # Metodo Constructor
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
    # Metodo agregar la clase Libro a la lista biblioteca
    def agregar(self, biblioteca):
        biblioteca.append(self)
        print(f"Libro '{self.titulo}' agregado con éxito.")
    # Metodo prestar cambia el estado de disponible (False) prestado o presenta estado de disponible
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")
    # Metodo devolver cambia el estado de disponible (True) devuelto o presenta estado de disponible
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto con éxito.")
        else:
            print(f"El libro '{self.titulo}' ya está disponible.")

def menu():
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    print("1. Agregar libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Mostrar libros")
    print("5. Buscar libro por ISBN")
    print("6. Salir")
    return input("Elige una opción: ")

def main():
    biblioteca = []

    while True:
        opcion = menu()

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            libro_nuevo = Libro(titulo, autor, isbn)
            libro_nuevo.agregar(biblioteca)

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

        elif opcion == "4":
            if not biblioteca:
                print("No hay libros en la biblioteca.")
            else:
                for libro in biblioteca:
                    if libro.disponible:
                        disponible = "Sí"
                    else:
                        disponible = "No"
                    print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {disponible}")

        elif opcion == "5":
            isbn = input("Ingresa el ISBN: ")
            for libro in biblioteca:
                if libro.isbn == isbn:
                    if libro.disponible:
                        disponible = "Sí"
                    else:
                        disponible = "No"
                    print(f"- {libro.titulo} ({libro.autor}) - ISBN: {libro.isbn} - Disponible: {disponible}")
                else:
                    print(f"No se encontró ningún libro con el ISBN {isbn}.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()