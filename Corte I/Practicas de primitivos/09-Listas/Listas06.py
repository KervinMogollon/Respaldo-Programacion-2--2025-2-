def numeros():
    return [1, 2, 18, 12, 24, 30, 6, 72, 106, 65, 99, 45]

cantidadNumeros = len(numeros())

def numerosPares():
    return [num for num in numeros() 
            if num % 2 == 0]

def numerosImpares():
    return [num for num in numeros() if num % 2 != 0]

def numeroMayor():
    return max(numeros())

def numeroMenor():
    return min(numeros())

def filtroNumerosMayoresQue(num):
    return [n for n in numeros() if n > num]

def sumaNumeros():
    return sum(numeros())

def promedioNumeros():
    if cantidadNumeros > 0:
        return sumaNumeros() / cantidadNumeros
    else:
        return 0

def intervaloNumeros(numMin, numMax):
    return [num for num in numeros() 
            if numMin <= num <= numMax]



print("los numeros pares dentro de la lista son:", numerosPares())
print("los numeros impares dentro de la lista son:", numerosImpares())
print("el numero mayor dentro de la lista es:", numeroMayor())
print("el numero menor dentro de la lista es:", numeroMenor())
print("los numeros mayores que 30 son:", filtroNumerosMayoresQue(30))
print("la suma de los numeros dentro de la lista es:", sumaNumeros())
print("el promedio de los numeros dentro de la lista es:", promedioNumeros())
print("los numeros dentro del intervalo dado son:", intervaloNumeros(10, 50))

