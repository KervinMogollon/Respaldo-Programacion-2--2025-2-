materia = input(f"Ingrese el nombre de la materia: ")
seccion = int(input(f"Ingrese la sección de la materia de {materia}: "))
numeroAlumnos = int(input(f"Ingrese el número de alumnos: "))

aprobados = 0
reprobados = 0
revision = 0

#aqui se usa como rango un valor variable dado por teclado, en este ejemplo se usa la variable numeroAlumnos
for i in range(numeroAlumnos):
    nombreAlumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota = float(input(f"Ingrese la nota de {nombreAlumno}: "))
    if nota < 0 or nota > 100:
        print(f"\nLa nota ingresada para {nombreAlumno} es invalida, \ndebe estar entre 0 y 100.")
        revision += 1
    elif nota >= 60:
        print(f"\n{nombreAlumno} aprobó.")
        aprobados += 1
    else:
        print(f"\n{nombreAlumno} reprobó.")
        reprobados += 1

print(f"\nResumen de la materia {materia} - Sección {seccion}:")
print(f"Total de alumnos aprobados: {aprobados}")
print(f"Total de alumnos reprobados: {reprobados}")
print(f"Total de alumnos a la revisión de notas: {revision}")
#esta f antes de las "" indica que es un string formateado, es decir, permite insertar variables directamente en
#el string