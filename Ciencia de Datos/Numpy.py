import numpy as np

#Crear array con numeros primos a partir de una lista
lista_primos = [2,3,5,7,11,13,17,19,23,29]
array_primos = np.array(lista_primos)
print(array_primos)

print()

#Crear un array con zeros
array_zeros = np.zeros(10)
print(array_zeros)

print()

#Crear un array con un rango de numeros
array_numeros = np.arange(10)
print(array_numeros)

print()

#Crear un array con una sucesion de numeros
array_pares = np.arange(0,20,2)
print(array_pares)

print()

#Dimensionar un array. Ejemplo 2x5
array_2x5 = array_pares.reshape(2,5)
print(array_2x5)

print()

#Suma de arrays de 1D
array_impares = array_pares + 1
print(array_impares)

print()

#Multiplicar arrays de 1D
print(array_numeros * 100)

print()

#Resta de arrays de 1D
print(array_impares - array_pares)

print()

#Metodos estadisticos
#Suma
print(array_primos.sum())

print()

#promedio
print(array_primos.mean())

print()

#Varianza
print(array_primos.var())

print()

#Ordenamiento de menor a mayor
array_fibonacci = np.array([55,0,144,1,21,89,5,8,13,1,34,3,2])
print(np.sort(array_fibonacci))

print()

#Ordenamiento de mayor a menor
print(-np.sort(-array_fibonacci))

print()

#Seleccionado de elementos. Ejemplo 2D
print(array_2x5[1,3])

print()

#Seleccionar varios elementos. Fila
print(array_2x5[0,:])

print()

#Seleccionar varios elementos. Columna
print(array_2x5[:,2])

print()

#Filtrar por una condicion 
print(array_fibonacci[array_fibonacci < 20])
