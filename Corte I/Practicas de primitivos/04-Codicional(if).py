nota01 = int(input("Ingrese la nota 01: "))
nota02 = int(input("Ingrese la nota 02: "))
nota03 = int(input("Ingrese la nota 03: "))

notaTotal = nota01 + nota02 + nota03
print(f"La nota total es: {notaTotal}")

if notaTotal < 0 or notaTotal > 100:
    print("La nota ingresada es incorrecta, debe estar entre 0 y 100.")
elif notaTotal >= 60:
    print("El estudiante está aprobado.")
elif notaTotal >= 40:
    print("El estudiante Tiene optativa a repetir en el examen con menor nota.")
else:
    print("El estudiante está reprobado.")
print("\n\nFin de la Evaluacion de Notas")