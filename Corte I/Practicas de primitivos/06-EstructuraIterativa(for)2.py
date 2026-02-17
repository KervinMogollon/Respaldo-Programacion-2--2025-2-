#se pueden generar ordenes y condicionales dentro del ciclo
for i in range(20):
    if i == 0:
        print(i, "es un número neutro")
    elif i % 2 == 0:
        print(i, "es un número par")
    else:
        print(i, "es un número impar")
    

print()
#para generar una lista de números primos
print("Los siguientes números son primos:")
for i in range(1,100):
    esPrimo = True
    for j in range(2,i):
        if i % j == 0:
            esPrimo = False
            break
    if esPrimo and i != 1:
        print(i)