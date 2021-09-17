import os

def Potencia (a,b):
    if(b==0):
        return 1
    else:
        return(a*Potencia(a,b-1))

def Factorial (a):
    if(a==0):
        return 1
    else:
        return(a*Factorial(a-1))

def convertidor_decimal_binario(decimal):
	cadena = "01"
	if decimal < 2:
		return cadena[decimal]
	else:
		return convertidor_decimal_binario(decimal//2) + cadena[decimal % 2]

os.system("cls")
print("Potencia y Factorial con funciones recursivas")
a=int(input("Ingrese la variable a: "))
b=int(input("Ingrese la variable b: "))
c=int(input("Ingrese la variable c: "))
n=int(input("Ingrese la variable n: "))
print("La operacion de a ^ b = ", Potencia(a,b))
print("La operacion de c! = ", Factorial(c))
print("El numero n en binario es: ", convertidor_decimal_binario(n))
os.system("Pause")
