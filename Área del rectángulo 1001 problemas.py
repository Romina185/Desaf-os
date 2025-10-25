#Calcular el área del recutángulo.
def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("⚠️  Por favor ingrese un número positivo.")
            else:
                return valor
        except ValueError:
            print("❌ Error: debe ingresar un número válido.")

# Expresar la  base y altura
base = pedir_numero("Ingrese la base del rectángulo: ")
altura = pedir_numero("Ingrese la altura del rectángulo: ")

# Calcular el área
area = base * altura

# Imprimir el resultado
print(f"✅ El área del rectángulo es: {area:.2f}")