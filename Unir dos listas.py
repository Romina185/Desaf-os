#Escribir un programa en Python que una dos listas
lista1 = [5, 6, 7]
lista2 = [8, 9, 10]
# Primer lista copiada
lista_unida = lista1.copy()
# Unir aplicando extend()
lista_unida.extend(lista2)
print("Lista unida con 'extend()':", lista_unida)