nombresEstudiante = []

for i in range(3):
    print()
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}:")
    nombresEstudiante.append(nombre)
    print(nombresEstudiante)
    
print()

materias = []

masMaterias = "si"
while masMaterias == "si":
    print()
    materia = input("Ingrese el nombre de la materia:")
    materias.append(materia)
    print(materias)
    masMaterias = input("¿Desea ingresar otra materia? (si/no):").lower()
    
