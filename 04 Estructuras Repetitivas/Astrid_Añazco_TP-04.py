#Práctico	4:	Estructuras	repetitivas
#Objetivo:	
#Implementar ciclos para resolver problemas que requieran repetición de acciones.

#Actividades 
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

for i in range(101):
    print(i)
    
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

# Forma a)
num = int(input("Ingrese un numero entero: "))

#si el usuario ingresa un numero negativo lo paso a positivo
if num < 0 :
    num = num * -1

contador = 0

while num > 0:
    num = num // 10 #esto elimina el ultimo digito
    contador +=1
    
#si el num es 0
if contador == 0:
    contador = 1
    
print(f"Cantidad de digitos: {contador}")

#Forma b)
#Tambien puedo hacerlo utilizando len 

num = int(input("Ingrese un numero entero: "))

#si el usuario ingresa un numero negativo lo paso a positivo
if num < 0 :
    num = num * -1

cant_digitos = len(str(num))

print(f"Cantidad de digitos: {cant_digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))



contador = 0
if num1 < num2:
    for i in range(num1+1,num2) :
        contador += i

else:
    for i in range(num2+1, num1): 
        contador += i
    
print(f"La suma entre todos los numeros comprendidos entre {num1} y {num2} excluyendolos es : {contador}.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 
print("Este programa suma en secuencia los numeros ingresados.")
print("Para finalizar y mostrar el total acumulado, ingrese 0.")

num = int(input("Ingrese el primer numero (distinto de cero): "))

acumulador = 0
while num != 0 :
    acumulador += num
    num = int(input("Ingrese el siguiente numero: "))
    
print(f"El resultado final es : {acumulador}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
print("!Juguemos!, estoy pensando un numero, adivina cual es...")
num = int(input("Ingresa un numero del 0 al 9: "))
aleatorio = random.randint(0,9)

acumulador = 1

while num != aleatorio :
    acumulador += 1
    num = int(input("¡Ups! Fallaste, ingresa un numero del 0 al 9: "))
        
print(f"¡Adivinaste!, el numero era {aleatorio}, lo lograste en {acumulador} intento(s).")       


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero entero positivo: "))

#verifico la condicion 
while num < 0:
    num = int(input("Numero invalido. Ingrese un numero entero positivo: "))

suma = 0
for i in range(0,num+1) :
    suma += i

print(f"El resultado de suma de los numeros comprendidos entre 0 y {num}, es : {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

acumulador = 0  
par = 0
impar = 0
positivo = 0
negativo = 0
     
while acumulador < 100 : 
    num = int(input("Ingrese un numero entero: "))
    acumulador += 1
    if num >= 0 :
        positivo += 1
    else : 
        negativo += 1
    if num % 2 == 0 :
        par += 1
    else :
        impar += 1

print("De los 100 numeros ingresados: ")
print(f"{par} son pares")
print(f"{impar} son impares")
print(f"{positivo} son positivos")
print(f"{negativo} son negativos")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).

contador = 0
suma = 0
while contador < 100 :
    num = int(input("Ingrese un numero: "))
    contador +=1
    suma += num
    
media = suma / 100

print(f"La media de los numeros ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = input("Ingrese un numero: ") #ingreso el numero como cadena para poder recorrerlo
num_nuevo = ""

for i in num :
    num_nuevo = i + num_nuevo  #lo guarda de atras para adelante
    
print(num_nuevo)