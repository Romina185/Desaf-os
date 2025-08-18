#Se amplia la clase de autor
class Autor:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = [] 

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def obtener_libros(self):
        return list(self.__libros) 

    # Método para agregar un libro
    def agregar_libro(self, libro):
        if libro not in self.__libros:
            self.__libros.append(libro)
            print(f"Libro '{libro}' agregado.")
        else:
            print(f"El libro '{libro}' ya está en la lista.")

    # Eliminar un libro
    def eliminar_libro(self, libro):
        if libro in self.__libros:
            self.__libros.remove(libro)
            print(f"Libro '{libro}' eliminado.")
        else:
            print(f"El libro '{libro}' no se encuentra en la lista.")

    # Representación del autor
    def __str__(self):
        return f"Autor: {self.__nombre}, Libros: {', '.join(self.__libros) if self.__libros else 'Ninguno'}"

# Ejemplo
autor1 = Autor("Gabriel Rolón")
autor1.agregar_libro("La Felicidad")
autor1.agregar_libro("El Duelo")
print(autor1)

autor1.eliminar_libro("El Duelo")
print(autor1)

print("Libros actuales:", autor1.obtener_libros())