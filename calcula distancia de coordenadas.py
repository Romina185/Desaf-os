import math  
#Función para calcular la distancia entre dos coordenadas
def calcular_distancia(punto1, punto2):
    """
    Calcula la distancia euclidiana entre dos puntos.
    punto1 y punto2 deben ser tuplas o listas con dos elementos (x, y).
    """
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#Función para interactuar con el usuario
def main():
    try:
        x1 = float(input("Ingrese x1: "))
        y1 = float(input("Ingrese y1: "))
        x2 = float(input("Ingrese x2: "))
        y2 = float(input("Ingrese y2: "))
        
        distancia = calcular_distancia((x1, y1), (x2, y2))
        print(f"La distancia entre los puntos es: {distancia}")
        #Ejemplo de la función
    except ValueError:
        print("Error: Por favor ingrese números válidos.")
#Ejecución del programa
if __name__ == "__main__":
    main()
