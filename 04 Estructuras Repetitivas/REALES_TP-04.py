#Ejercicio 1

for i in range(1, 101):
    print(i)

#Ejercicio 2

numero = int(input("Ingrese un número entero: "))

cantidad_digitos = 0

while numero > 0:
    numero //= 10
    cantidad_digitos += 1

print("La cantidad de dígitos es:", cantidad_digitos)

#Ejercicio 3

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

suma = 0
for i in range(inicio + 1, fin):
    suma += i

print(f"La suma de los números entre {inicio} y {fin} es:", suma)

#Ejercicio 4

total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    total += numero

print(f"La suma total es: {total}")

#Ejercicio 5

import random

numero_secreto = random.randint(0, 9)

intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
        break

#Ejercicio 6

for i in range(100, 0, -2):
    print(i)

#Ejercicio 7

numero = int(input("Ingrese un número entero positivo: "))
total = 0

for i in range(0, numero):
    total += i

print(f"La suma de los números desde 0 hasta {numero - 1} es:", total)

#Ejercicio 8

cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#Ejercicio 9

cantidad_numeros = 100

suma = 0

for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad_numeros
print(f"La media de los números ingresados es: {media}")

#Ejercicio 10

numero = int(input("Ingrese un número entero: "))
numero_original = abs(numero)
inverso = 0

while numero_original > 0:
    digito = numero_original % 10
    inverso = inverso * 10 + digito
    numero_original //= 10

if inverso == numero:
    print(f"El número {numero} es capicúa.")

if numero < 0:
    inverso = -inverso

print(f"El inverso de {numero} es: {inverso}")