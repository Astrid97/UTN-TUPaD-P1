# Ejercicios  
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(num):
    if num == 0:
        return 0
    else :
        return num+factorial(num-1)
    
num = int(input("Ingrese un numero: "))
print(factorial(num))


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else: 
        return fibonacci(posicion-1)+fibonacci(posicion-2)

num = int(input("Ingrese el numero de la posicion: "))
for i in range(num): 
    print(f"En la posicion {i} obtengo el valor de : {fibonacci(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)
    
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.
 
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
# procedimiento: 
# 1. Dividir el número por 2. 
# 2. Guardar el resto (0 o 1). 
# 3. Repetir el proceso con el cociente hasta que llegue a 0. 
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

def binario(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return binario(num//2) + str(num%2)
    
num = int(input("Ingrese un numero positivo entero: "))
print(f"El numero {num} equivale a {binario(num)} en binario")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra [0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese un palabra: ")
condicion = es_palindromo(palabra)
if condicion is True:
    print(f"La palabra {palabra} es palindromo.")
else: 
    print(F"La palabra {palabra} NO es palindromo.")
    
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    if n < 10:
        return n
    else: 
        return n % 10 + suma_digitos(n // 10)

print (suma_digitos(444))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
 
#       Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
base = 10
print(contar_bloques(base))


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
#       Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0  
   
def contar_digito(numero, digito):
# Caso base
    if numero == 0:
        return 0
    # Obtener el último dígito del número
    ultimo = numero % 10
    # Comparar con el dígito que buscamos
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
print(contar_digito(5555, 5))