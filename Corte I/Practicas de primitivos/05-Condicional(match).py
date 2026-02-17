nombreTrabajador = input("Ingrese el nombre del trabajador: ")
tipoTrabajador = int(input("Ingrese el tipo de trabajador (1: gerente, 2: obrero, 3: administrativo, 4: mecanico): "))

cargoTrabajador = ""
match tipoTrabajador:
    case 1:
        cargoTrabajador = "Gerente"
    case 2:
        cargoTrabajador = "Obrero"
    case 3:
        cargoTrabajador = "Administrativo"
    case 4:
        cargoTrabajador = "Mecanico"
    case _:
        print("Tipo de trabajador no valido.")

print(f"\nEl trabajador {nombreTrabajador} es un {cargoTrabajador}")

sueldo = float(input(f"\nIngrese el sueldo actual del {cargoTrabajador} {nombreTrabajador}: "))

nuevoSueldo = 0

match cargoTrabajador:
    case "Gerente":
        nuevoSueldo = sueldo * 1.10
    case "Obrero":
        nuevoSueldo = sueldo * 1.20
    case "Administrativo":
        nuevoSueldo = sueldo * 1.20
    case "Mecanico":
        nuevoSueldo = sueldo * 1.22
    case _:
        nuevoSueldo = sueldo

print(f"\nEl nuevo sueldo del {cargoTrabajador} {nombreTrabajador} es: {nuevoSueldo}$")