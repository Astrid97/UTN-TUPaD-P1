# Práctico 5: Listas 
# Objetivo:  
# Desarrollar la comprensión y la capacidad de manipular listas en Python 
# mediante la aplicación de conceptos fundamentales como la indexación, la 
# modificación de elementos, el uso de métodos integrados y el manejo de 
# listas anidadas.

# Actividades  
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
# range. 

lista = list(range(4,101,4))
print(lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos!

mi_lista = ["gato","milanesas","empanadas","perfumes","novio"]
print(mi_lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
# ejemplo: 
# lista_vacia = []

lista = []

lista.append("banana")
lista.append("frutilla")
lista.append("cereza")
print(lista)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

# max(num) encuentra el valor mas grande de la lista, en este caso 22,
# num.remove elimina el 22 de la lista y luego se imprime la lista final: [8,15,3,7]

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros.

numeros = list(range(10,31,5))

print(numeros[0])
print(numeros[1])

#tambien puedo usar Slicing
#lista[inicio:fin]

print(numeros[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"] 

autos[1] = "focus"
autos[2] = "etios"

print(autos)

#usando slicing

autos[1:3] = ["corolla", "sw4"]

print(f"Con slicing: {autos}")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla.

#opcion 1
dobles1 = []

dobles1.append(5*2)
dobles1.append(10*2)
dobles1.append(15*2)

print(dobles1)


#opcion 2

dobles2 = []

for num in [5,10,15]:
    dobles2.append(num*2)
    
print(dobles2)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla. 

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.

lista_anidada = []
lista_anidada.append(15)
lista_anidada.append(True)

posicion2 = [25.5,57.9,30.6]

lista_anidada.append(posicion2)
lista_anidada.append(False)

print(lista_anidada)