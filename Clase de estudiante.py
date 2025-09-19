#Crear una clase Estudiante de estudiante.
class Estudiante:
    def __init__(self, nombre, edad, grado, notas):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.notas = notas
        self.promedio = sum(notas) / len(notas)
#Elaborar una lista
estudiantes = [
    Estudiante("Carolina", 15, "10°", [8, 7, 9, 10, 6]),
    Estudiante("Lucía", 14, "9°", [9, 9, 10, 10, 9]),
    Estudiante("Mateo", 16, "11°", [6, 5, 7, 6, 6]),
]
# Ordenar por promedio (de mayor a menor)
estudiantes_ordenados = sorted(estudiantes, key=lambda e: e.promedio, reverse=True)
#Expresar la lista ordenada.
for est in estudiantes_ordenados:
    print(f"{est.nombre}, {est.edad} años, Grado: {est.grado}, Promedio: {est.promedio:.2f}")

