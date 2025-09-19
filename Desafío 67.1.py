try:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    
    resultado = num1 / num2
    print(f"✅ Resultado de la división: {resultado}")

except ValueError:
    print("❌ Error: Debes ingresar solo valores numéricos enteros.")

except ZeroDivisionError:
    print("❌ Error: No se puede dividir entre cero.")