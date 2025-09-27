#Construir un árbol binario simple.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None  # corregido
#Se define el recorrido en preorden
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)
# Expresar el árrbol
# Nivel 1
raiz = Nodo(12)

# Nivel 2
raiz.izquierda = Nodo(7)
raiz.derecha = Nodo(6)

# Nivel 3
raiz.izquierda.izquierda = Nodo(5)
raiz.izquierda.derecha = Nodo(4)

raiz.derecha.izquierda = Nodo(2)
raiz.derecha.derecha = Nodo(3)

# Probar recorrido en preorden
preorden(raiz)

print("recorrido en preorden:")