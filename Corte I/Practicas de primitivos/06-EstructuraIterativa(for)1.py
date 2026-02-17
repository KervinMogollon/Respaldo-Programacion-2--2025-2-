frutas = ["manzana", "banana", "cereza"] #los [] son una lista o array
for fruta in frutas:
    print("Me gusta la", fruta)

print()

#la x dentro del () del range controla el las veces que se va a repetir el bucle
for i in range(5):
    print("Número del bucle 1:", i)

print()

i = 1
for i in range(8):
    print("Número del bucle 1:", i)

print()

x = 10
for i in range(x):
    print("Número del bucle 2:", i + 2)

print()

#tambien se pueden hacer operaciones al i del bucle
for i in range(15):
    print("Número del bucle del 1 al 15 * 2:", i * 2)

print()

#Puedes usar range(inicio, fin, paso) para más control. donde "paso" es el incremento o multiplo que controla el incremento
for i in range(0, 10, 2):
    print("Número par:", i)
    
print()
    
for i in range(0, 10, 3):
    print("Número impar:", i)

print()

for i in range(12, 100, 5):
    print("Número múltiplo de 5:", i)

print()

for i in range(0, 100, 9):
    print("Número múltiplo de 9:", i)
