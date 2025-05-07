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
    