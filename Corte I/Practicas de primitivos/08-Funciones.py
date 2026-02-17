#funciones, tambien conocidas como metodos, son bloques de codigo que realizan una tarea especifica

def inpNombre():
    return input("Por favor, ingresa tu nombre: ")
 
def saludo():
    return "Hola, ¿cómo estás?\n\n"

def despedida():
   return print("Adiós, que tengas un buen día!\n")

def suma(a, b) -> float: 
    #typeamos con float para que acepte decimales, como tal lo que puede ir (ya que es opcional)
    #luego de -> sirve para indicar el tipo de dato que se espera como resultado
    return a + b

def resta():
    c = float(input("Ingrese el primer número: "))
    d = float(input("Ingrese el segundo número: "))
    #es importante aclarar que cualquier input o print dentro de una funcion no se ejecura en consola a menos que la
    #funcion sea llamada
    return f"la resta de {c} y {d} es: {c - d}"
    #esta f antes de las "" indica que es un string formateado, es decir, permite insertar variables directamente en
    #el string

def bienvenidaNombre():
    return f"¡Bienvenido/a {nombre}!\n"

print("Vamos a interactuar usando funciones.\n")
print("Primero, necesito saber tu nombre.")
nombre = inpNombre()

print(saludo())
print(bienvenidaNombre())

print(f"Ok {nombre}, sumemos dos números de tu preferencia.\n")
x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
print(f"La suma de {x} y {y} es: {suma(x, y)}\n")

print("Ahora resta dos números.\n")
print(resta())
#por un lado la suma() funciona haciendo la suma de numero dados por parametro que son llenados por teclado fuera de la funcion
#por otro lado la resta() pide los numeros por teclado dentro de la funcion

despedida()