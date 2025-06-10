#Definir si un número es primo
#Ingresar el número entero
numero = int(input("Ingresa un número entero:"))
#Uilizar las condicionales
if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")
