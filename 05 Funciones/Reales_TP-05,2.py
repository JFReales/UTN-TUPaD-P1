## Main

def imprimir_hola_mundo():
    print("¡Hola, mundo!")

def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

def tabla_mulplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return suma, resta, multiplicacion, division

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

## Programa Principal

#Ejercicio 1

mensaje = imprimir_hola_mundo()

#Ejercicio 2

nombre_usuario = input("Ingresa tu nombre: ")
saludar_usuario(nombre_usuario)

#Ejercicio 3

datos_personales = input("Ingresa tus datos personales (nombre, apellido, edad, residencia) separados por comas: ")
informacion_personal(*datos_personales.split(','))

#Ejercicio 4

radio = float(input("Ingresa el radio del círculo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo es: {area}")
perimetro = calcular_perimetro_circulo(radio)
print(f"El perímetro del círculo es: {perimetro}")

#Ejercicio 5

segundos = int(input("Ingresa el número de segundos: "))
horas, minutos, segundos_restantes = segundos_a_horas(segundos)
print(f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos")

#Ejercicio 6

numero = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
tabla_mulplicar(numero)

#Ejercicio 7

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

#Ejercicio 8

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

#Ejercicio 9
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celcius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

#Ejercicio 10
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: ")) 
c = float(input("Ingresa el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los números es: {promedio:.2f}")





