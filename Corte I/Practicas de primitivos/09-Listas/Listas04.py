def inventarioVerduras():
    return ["lechuga", "espinaca", "zanahorias"]

def agregarVerdura(verdura):
    inventario = inventarioVerduras()
    inventario.append(verdura)
    print(f"\nInventario actualizado: {inventario}")
    return inventario

print("Inventario de verduras:", inventarioVerduras())

respuesta = input("\n¿Desea agregar otra verdura? (si/no): ")
while respuesta.lower() == "si":
    verdura = input("\nIngrese la verdura que desea agregar al inventario: ")
    inventario = agregarVerdura(verdura)
    respuesta = input("\n¿Desea agregar otra verdura? (si/no): ")
