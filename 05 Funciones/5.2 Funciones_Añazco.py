# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal

def imprimir_hola_mundo():
    print("Hola Mundo!")

#programa principal    
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de￾volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print (f"Hola {nombre}!")


usuario = input("Ingrese su nombre: ")
saludar_usuario(usuario)   

# 3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pe￾dir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
    
#programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese el lugar donde vive: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra￾dio como parámetro 
# y devuelva el área del círculo. calcular_peri￾metro_circulo(radio) que reciba el radio 
# como parámetro y devuel￾va el perímetro del círculo. 
# Solicitar el radio al usuario y llamar am￾bas funciones para mostrar los resultados.

import math 
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

radio = float(input("Ingrese el radio del circulo: "))
print(f"El area del circulo es: {calcular_area_circulo(radio)}, y el perimetro es: {perimetro_circulo(radio)}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos￾trar el resultado usando esta función.

def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora

segundos = int(input("Ingrese la cantidad de segundos: "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.") 

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun￾ción.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
        
num = int(input("Tabla de multiplicar del numero: "))
tabla_multiplicar(num)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta￾do de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los re￾sultados de forma clara.

def operaciones_basicas(a, b):
    print(f"Suma = {a+b}")
    print(f"Resta = {a-b}")
    print(f"Multiplicacion = {a*b}")
    print(f"Division = {a/b}")
    
operaciones_basicas(10, 5)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun￾ción para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {fahrenheit}")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio es: {promedio}")