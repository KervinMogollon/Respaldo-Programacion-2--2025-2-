"""
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

print("***********************************************************************")
print("***********************************************************************")
print("*********************Program: Password*********************************")
print()

password=input("Please enter a password: ")
print()
print("Password stored!!!")

invalid = True
while invalid: 
    passwordRead = input("Please enter the password stored:")
    if password.lower()==passwordRead.lower():
        print("Congratulations!!!")
        invalid=False
    else:
        print("Error!!! Invalid Password!!!")

print("***********************************************************************")
print("***********************************************************************")
print("**********************END OF PROGRAM***********************************")