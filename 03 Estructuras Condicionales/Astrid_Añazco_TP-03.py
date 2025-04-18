#Práctico 3: Estructuras condicionales 
# Objetivo:  
# Comprender y aplicar las estructuras condicionales en la programación, 
# desarrollando algoritmos que involucren tomas de decisiones.  

# Actividades : 

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
  
edad = int(input("Por favor, ingrese su edad: "))

if edad > 18 :
    print("Es mayor de edad") 

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”.

nota = int(input("Por favor, ingrese su nota: "))

if nota >= 6 :
    print("Aprobado.")
else:
    print("Desaprobado.")
    
# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar. 

num = int(input("Por favor, ingrese un numero par: "))

while  num % 2 != 0 :
    num = int(input("Por favor, ingrese un numero par: "))

print("Usted ha ingresado un numero par.")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. 

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12 :
    print("Es un niño/a.")
elif edad >= 12 and edad < 18 :
    print("Es un adolescente.")
elif edad >= 18 and edad < 30 :
    print("Es un adulto/a joven.")
else : 
    print("Es un adulto")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

contrasenia = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")

while len(contrasenia) < 8 or len(contrasenia) > 14 :
    contrasenia = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")

print("Ha ingresado una contraseña correcta.")

    



