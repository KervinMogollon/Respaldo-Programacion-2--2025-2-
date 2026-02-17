listasMateriales = ["hojas", "lapices", "cuadernos"]

print("Lista de materiales:", listasMateriales)

respuesta = input("\n¿Desea agregar otro material? (si/no): ")
while respuesta.lower() == "si":
    material = input("\nIngrese el material que desea agregar a la lista: ")
    listasMateriales.append(material)
    print(f"\nLista actualizada: {listasMateriales}")
    
    respuesta = input("\n\n¿Desea agregar otro material? (si/no): ")