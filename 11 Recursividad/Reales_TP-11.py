#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Ingrese un número entero positivo: "))
print(f"El factorial de {num} es {factorial(num)}")

#Ejercicio 2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Ingrese un número entero positivo: "))
print(f"El término {n} de la serie de Fibonacci es {fibonacci(n)}")

#Ejercicio 3
def calc_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / calc_potencia(base, -exponente)
    else:
        return base * calc_potencia(base, exponente - 1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es {calc_potencia(base, exponente)}")

#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
n = int(input("Ingrese un número entero: "))
print(f"El número {n} en binario es: {decimal_a_binario(n)}")

#Ejercicio 5
def es_palindromo(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return es_palindromo(s[1:-1])
    
texto = input("Ingrese una cadena de texto: ")
if es_palindromo(texto):
    print(f"La cadena '{texto}' es un palíndromo.")
else:
    print(f"La cadena '{texto}' no es un palíndromo.")

#Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
n = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {n} es {suma_digitos(n)}")

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

n = int(input("Ingrese un número entero positivo: "))
print(f"El número de bloques necesarios para construir una pirámide de {n} niveles es: {contar_bloques(n)}")

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    elif numero < 0:
        numero = -numero
    
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
  
numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese el dígito a contar(0 al 9): "))
if 0 <= digito <= 9:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
else:
    print("El dígito debe estar entre 0 y 9.")

