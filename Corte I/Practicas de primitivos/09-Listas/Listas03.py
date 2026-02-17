def inventarioFrutas():
    inventario = ["manzanas", "bananas", "naranjas"]
    print("Inventario de frutas:", inventario)

    respuesta = input("\n¿Desea agregar otra fruta? (si/no): ")
    while respuesta.lower() == "si":
        fruta = input("\nIngrese la fruta que desea agregar al inventario: ")
        inventario.append(fruta)
        print(f"\nInventario actualizado: {inventario}")

        respuesta = input("\n¿Desea agregar otra fruta? (si/no): ")

print(inventarioFrutas())