#Crear una clase de libro con atributos privados.
class Libro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
#Definir el método getter.
    @property
    def titulo(self):
        return self._titulo
# Aplicar el método setter para modificar el título.
    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, valor):
        self._autor = valor
    @property
    def isbn(self):
        return self._isbn
    @isbn.setter
    def isbn(self, valor):
        self._isbn = valor
libro = Libro("Felicidad", "Gabriel Felipe Rolón", "97895049826")
# Acceder a los atributos.
print(libro.titulo)
print(libro.autor)
print(libro.isbn)
# Modificar los atributos.
libro.titulo = "La Felicidad"
libro.autor = "Gabriel Rolón"
libro.isbn = "9789504976752"
#Imprimir.
print(libro.titulo)
print(libro.autor)
print(libro.isbn)