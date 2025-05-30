#Ejercicio 1

lista = list(range(4, 101, 4))
print(lista)

#Ejercicio 2

lista = ["Futbol", "Gatos", "Padel", "Cerveza", "Dormir"]

penultimo = lista[-2]
print(penultimo)

#Ejercicio 3

lista = []
lista.append("Futbol")
lista.append("Gatos")
lista.append("Padel")

print(lista)

#Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#Ejercicio 5
#Al correr el programa podemos ver que se elimina el elemento con el valor 22, ya que es el mayor de la lista.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Ejercicio 6

lista = list(range(10, 31, 5))

print(lista[0:2])

#Ejercicio 7

autos = ["Sedan", "Polo", "Suran", "Gol"]

autos[1] = "Civic"
autos[2] = "Corolla"

print(autos)

#Ejercicio 8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10

lista_anidada = [[0], [True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)