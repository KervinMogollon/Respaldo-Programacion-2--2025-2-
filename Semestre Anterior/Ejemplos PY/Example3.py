"""Solicitar al usuario que ingrese los nombres de dos personas, los cuales se
almacenarán en dos variables. A continuación, imprimir “ si los nombres de ambas
personas comienzan con la misma letra o si terminan con la misma letra Si no es así,
imprimir “no hay coincidencia”"""

print("***********************************************************************")
print("***********************************************************************")
print("*********************Program: Names Match******************************")
print()
name1 = input("Please enter the name #1: ")
name2 = input("Please enter the name #2: ")
last1 = len(name1)
last2 = len(name2)

if (name1[0] == name2[0]) or (name1[-1]==name2[-1]):
#if (name1[0] == name2[0]) or (name1[last1-1]==name2[last2-1]):
    print()
    print("The names match")
else:
    print()
    print("The names not match")
print()
print("***********************************************************************")
print("***********************************************************************")
print("**********************END OF PROGRAM***********************************")



