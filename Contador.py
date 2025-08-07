#Crear Una función recursiva cuenta_regresiva(n) que imprima los números desde n hasta 0, uno por línea.
#Se define la función solicitando un número positivo.
def cuenta_regresiva(n):
    if n == 0:
        print(0)  # Caso base: imprimimos 0 y terminamos
    else:
        print(n)
        cuenta_regresiva(-1)
