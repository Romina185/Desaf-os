#Crear una clase músico.
class Musico:
    def __init__(self, nombre):
        self._nombre = nombre
    #Definir el instrumento

    def instrumento(self):
        return f"{self._nombre} toca un instrumento genérico"

    def get_nombre(self):
        return self._nombre

# Subclase Guitarrista
class Guitarrista(Musico):
    def __init__(self, nombre):
        super().__init__(nombre)

    def instrumento(self):
        return f"{self._nombre} toca la guitarra"

# Subclase Baterista
class Baterista(Musico):
    def __init__(self, nombre):
        super().__init__(nombre)

    def instrumento(self):
        return f"{self._nombre} toca la batería"

# Función para demostrar el polimorfismo
def mostrar_instrumento(musico):
    print(musico.instrumento())

# Expresar los  objetos
guitarrista = Guitarrista("Romina")
baterista = Baterista("Eduardo")
musico_general = Musico("Alguien")

# Usar el polimorfismo y mostrar
mostrar_instrumento(guitarrista)   
mostrar_instrumento(baterista)       
mostrar_instrumento(musico_general)