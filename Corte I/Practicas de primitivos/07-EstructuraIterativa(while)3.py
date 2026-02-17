print("Bienvenido a esta calculadora basica")
respuesta = "si"
while respuesta == "si":
    numero1 = float(input("Ingrese el primer número: "))
    
    operacion = input("lista de operaciones validas:"
                      "\nsuma = +"
                      "\nresta = -"
                      "\nmultiplicación = *"
                      "\ndivisión = /"
                      "\npotencia = **"
                      "\nraices = **1/n"
                      "\nIngrese la operación a realizar: ")
    
    if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/":
        numero2 = float(input("Ingrese el segundo número: "))
    elif operacion == "**":
        numero2 = float(input("Ingrese el exponente: "))
    elif operacion == "**1/n":
        numero2 = float(input("Ingrese el índice de la raíz: "))
    else:
        print("Operación no válida.")
        continue

    print()
    
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("División por cero no permitida.")
            continue
    elif operacion == "**":
        resultado = numero1 ** numero2
    elif operacion == "**1/n":
        resultado = numero1 ** (1/numero2)
    else:
        print("Esta operación no es válida. Intente de nuevo.")
        continue
    
    print(f"\nEl resultado de {numero1} {operacion} {numero2} es: {resultado}")
    respuesta = input("¿Desea realizar otra operación? (si/no): ").lower()    