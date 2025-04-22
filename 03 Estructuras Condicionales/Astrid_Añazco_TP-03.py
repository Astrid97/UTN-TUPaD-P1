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

    
# 6) escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range (50)]
print(F"Lista: {numeros_aleatorios}")
      
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(F"moda: {moda}, mediana: {mediana}, media {media}")

if media > mediana and mediana > moda :
    print("Hay Sesgo Positivo o a la derecha")
elif media < mediana and mediana < moda :
    print("Hay Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda and moda == media :
    print("No hay Sesgo")
    
# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = input("Por favor, ingrese una frase o palabra: ")

vocales = "A,E,I,O,U,a,e,i,o,u"

ultima_letra = frase[-1]

if ultima_letra in vocales :
    frase += "!"

print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor, ingrese su nombre: ")

print("Opciones: ")
print("Escriba 1 Si quiere su nombre en mayúsculas.")
print("Escriba 2 Si quiere su nombre en minúsculas")
print("Escriba 3 Si quiere su nombre con la primera letra mayúscula")

opcion = int(input("Ingrese la opcion deseada (1 , 2 o 3): "))

while opcion not in [1,2,3]: 
    opcion = int(input("Ingrese la opcion deseada (1 , 2 o 3): "))
    
if opcion == 1 :
    print(nombre.upper())

elif opcion == 2 :
    print(nombre.lower())
    
else :
    print(nombre.title())
    
    
# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

print("Este programa clasifica la magnitud de los terremotos segun las categorias de la escala de Richter")

magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

if magnitud < 3 :
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4 :
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7 :
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7 :
    print("Extremo (puede causar graves daños a gran escala).")
    
# 10) Utilizando la información aportada Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

print("¿Desea saber en que estacion del año se encuentra?")

hemisferio = input("Ingrese el hemisferio (N para norte, S para sur): ").upper()
mes = int(input("Ingrese el numero del mes (1 a 12): "))
dia = int(input("Ingrese el dia del mes: "))

# verifico que el dia y mes sean validos
if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Fecha inválida.")
else:
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or mes in [10, 11] or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    #resultado según el hemisferio
    if hemisferio == "N":
        print("Usted se encuentra en", estacion_norte)
    elif hemisferio == "S":
        print("Usted se encuentra en", estacion_sur)
    else:
        print("Hemisferio no válido. Ingrese 'N' o 'S'.")