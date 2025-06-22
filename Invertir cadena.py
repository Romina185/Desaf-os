#Se define la cadena
def invertir_cadena(cadena):
    invertida = ''
#Expresar condicional
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida
#Agregar el texto
texto = "estamos en invierno"
texto_invertido = invertir_cadena(texto)
print(texto_invertido)