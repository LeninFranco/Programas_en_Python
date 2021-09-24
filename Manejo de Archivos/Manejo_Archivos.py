#Crear y Escribir un Archivo TXT

archi = open("datos.txt","w")

for i in range(1,11):
    archi.write(f"Linea numero {i}\n")

archi.write("Hola Mundo\n")
archi.write("Archivos en Python\n")

archi.close() #Importante cerrar el archivo para hacer otra operacion y que otro programa lo pueda ocupar

print("Contenido guardado correctamente")

print("-"*50)

#Leer todo el contenido 

archi = open("datos.txt","r")

contenido = archi.read()

print(type(contenido))
print(contenido)

archi.close() #Importante cerrar el archivo para hacer otra operacion y que otro programa lo pueda ocupar

print("-"*50)

#Leer linea por linea

archi = open("datos.txt","r")

for linea in archi:
    print(linea, end='')

archi.close() #Importante cerrar el archivo para hacer otra operacion y que otro programa lo pueda ocupar

print("-"*50)

#Guardar el contenido en una lista

archi = open("datos.txt","r")

lineas = archi.readlines()

print(type(lineas))

print(f"El archivo tiene {len(lineas)} lineas")

print(lineas)

archi.close() #Importante cerrar el archivo para hacer otra operacion y que otro programa lo pueda ocupar
