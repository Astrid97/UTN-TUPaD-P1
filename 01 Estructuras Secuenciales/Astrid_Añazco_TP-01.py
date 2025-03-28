#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
Saludo = print("Hola Mundo")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su lugar de residencia: ") 
print (F"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

import math
print("Este programa calcula el area y el perimetro de un circulo a partir de su radio.")
radio = float(input("Ingrese el radio de un circulo: "))
area = math.pi * radio **2
perimetro = 2  * math.pi * radio

print(f"El area del circulo es : {area}.")
print(f"el perimetro del circulo es : {perimetro}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.

segundos = int(input("Ingrese los segundos : "))
horas = segundos / 3600 
print(f"{segundos} segundos equivalen a {horas} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número. 

num = int(input("Ingrese un numero: "))
# se me ocurrio utilizar un ciclo MIENTRAS para hacer la tabla del 1 al 10
i = 1
print(f"Tabla del {num}")
while i <= 10 :
    print(f"{num} x {i} = {num * i}")
    i = i + 1

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1 = int(input("Ingrese un numero entero distinto de cero: "))
num2 = int(input("Ingrese otro numero entero distinto de cero: "))

print(f"Suma: {num1+num1}")
print(f"Division: {num1 / num2}")
print(f"Multiplicar: {num1 * num2}")
print(f"Restar: {num1-num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. 

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc =  peso / (altura**2)

print(f"Su indice de masa corporal es: {imc}")

#  9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahr = (9/5) * celsius + 32
print(f"{celsius} grados en Celsius equivalen a {fahr} grados en Fahrenheit.")

#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números.

# num1 = float(input("Ingrese el primer numero: "))
# num2 = float(input("Ingrese el segundo numero: "))
# num3 = float(input("Ingrese el tercer numero: "))

# promedio = (num1 + num2 + num3) / 3

# print(f"El promedio de los 3 numeros ingresados es: {promedio}")

