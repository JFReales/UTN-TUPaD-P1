# Ejercicio 1

edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Es menor de edad")

# Ejercicio 2

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3

par = int(input("Ingrese un número par: "))
if par % 2 == 0:
    print("El número es par")
else:
    print("Por favor ingrese un número par")

# Ejercicio 4

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Es niño/a")
elif edad >= 12 and edad < 18:
    print("Es adolescente")
elif edad >= 18 and edad < 30:
    print("Es adulto/a joven")
elif edad >= 30:
    print("Es adulto/a")

# Ejercicio 5

contraseña = input("Ingrese la contraseña de entre 8 y 14 caracteres: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Has ingresado una contraseña válida")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("La media es:", media)
print("La mediana es:", mediana)
print("La moda es:", moda)

if media > mediana and media > moda:
    print("Sesgo positivo")
elif media < mediana and media < moda:
    print("Sesgo negativo")
elif media == mediana and media == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo")

# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"

print("La frase es:", frase)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1. Mostrar nombre en mayúsculas")
print("2. Mostrar nombre en minúsculas")
print("3. Mostrar nombre con la primera letra en mayúscula")

opcion = int(input("Ingrese su opción: "))
if opcion == 1:
    print("Nombre en mayúsculas:", nombre.upper())  
elif opcion == 2:
    print("Nombre en minúsculas:", nombre.lower())
elif opcion == 3:
    print("Nombre con la primera letra en mayúscula:", nombre.capitalize())
else:
    print("Opción no válida")

# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del sismo: "))
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
elif 7 <= magnitud:
    print("Extremo")

# Ejercicio 10

hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
if hemisferio == "N":
    if (mes >= 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Es primavera")
    elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Es verano")
    elif (mes >= 9 and dia >= 21) or (mes <= 12 and dia <= 20):
        print("Es otoño")
    else:
        print("Es invierno")
elif hemisferio == "S":
    if (mes >= 3 and dia >= 21) or (mes <= 6 and dia <= 20):
        print("Es otoño")
    elif (mes >= 6 and dia >= 21) or (mes <= 9 and dia <= 20):
        print("Es invierno")
    elif (mes >= 9 and dia >= 21) or (mes <= 12 and dia <= 20):
        print("Es primavera")
    else:
        print("Es verano")
