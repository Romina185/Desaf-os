def contar_lineas(nombre_archivo):
    try:
        contador = 0
        with open(nombre_archivo, 'r') as archivo:  # abre y cierra automáticamente
            for linea in archivo:
                contador += 1
        return contador
    except FileNotFoundError:
        print(f"❌ Error: el archivo '{nombre_archivo}' no existe.")
        return 0

# Ejemplo de uso
archivo = "texto.txt"
print("Cantidad de líneas:", contar_lineas(archivo))
