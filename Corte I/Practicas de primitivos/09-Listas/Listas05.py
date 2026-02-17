def inventarioViveres():
    return ["arroz", "frijoles", "lentejas"]

def agregarViveres(inventario, viveres):
    inventario.append(viveres)
    print(f"\nInventario actualizado: {inventario}")
    return inventario

def eliminarViveres(inventario, viveres):
    if viveres in inventario:
        inventario.remove(viveres)
        print(f"\nInventario actualizado: {inventario}")
    else:
        print(f"\nEl víveres '{viveres}' no está en el inventario.")
    return inventario

def vaciarInventario(inventario):
    inventario.clear()
    print(f"\nInventario vaciado: {inventario}")
    return inventario

def operacionInventario():
    inventario = inventarioViveres()
    while True:
        print("\nOpciones:")
        print("1. Agregar víveres")
        print("2. Eliminar víveres")
        print("3. Vaciar inventario")
        print("4. Salir")

        opcion = input("\nSeleccione una opción (1-4): ")
        if opcion == "1":
            vive = input("Ingrese el víveres que desea agregar: ")
            inventario = agregarViveres(inventario, vive)
        elif opcion == "2":
            vive = input("Ingrese el víveres que desea eliminar: ")
            inventario = eliminarViveres(inventario, vive)
        elif opcion == "3":
            inventario = vaciarInventario(inventario)
        elif opcion == "4":
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción inválida.")

print("Bienvenido al sistema de gestión de inventario de víveres.")
print("Puede agregar, eliminar o vaciar el inventario según sus necesidades.\n")
print("Inventario actual de víveres:", inventarioViveres())
print()
print(operacionInventario())

