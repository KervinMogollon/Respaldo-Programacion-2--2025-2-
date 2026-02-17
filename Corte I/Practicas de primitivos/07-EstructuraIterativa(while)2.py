#un ejemplo con entrada por teclado donde si no se ingresa el valor correcto no se sale del ciclo
clave = "l"
while clave != "1234":
    clave = input("Introduce la clave: ")

print("¡Acceso concedido!")

#caso contrario, un caso de entrada por teclado que para salir del ciclo se debe ingresar un valor distinto 
#del valor de la condicion
i = 1
respuesta = "si"
while respuesta == "si":
    print(f"numero de Iteración {i}")
    i += 1
    respuesta = input("¿Desea Seguir aumentando el valor de la iteracion? (si/no): ")
print("¡Hasta luego!")