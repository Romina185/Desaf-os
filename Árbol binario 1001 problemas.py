#Construir un árol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
#Definir una funcion para verificar.
def es_BST(raiz):
    valores = []
#definir una función para recorrer el arbol en orden
    def inorder(nodo):
        if nodo:
            inorder(nodo.izquierda)
            print(nodo.valor, end=" ")  
            # imprime cada valor en orden
            valores.append(nodo.valor)
            inorder(nodo.derecha)

    inorder(raiz)
    print() 
     # salto de línea
    return all(valores[i] < valores[i+1] for i in range(len(valores)-1))
#Construcción del árbol
raiz = Nodo(8)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(9)
raiz.izquierda.izquierda = Nodo(1)
raiz.izquierda.derecha = Nodo(7)
raiz.derecha.derecha = Nodo(15)

# --- Ejecución ---
print("Recorrido en orden del árbol:")
resultado = es_BST(raiz)
print("¿Es un BST?:", resultado)