import os
os.system("cls")

print("Solo se acepta numeros del 0-9 y operadores +, -, *, /")
print("Ingrese la operacion que desea realizar: ")
Ecu = str(input())
Band = False

for i in Ecu:
    if(i.isdigit() or i == "+" or i =="-" or i == "*" or i == "/"):
        Band = True
    else:
        print("Solo se aceptan numeros y operadores basicos")
        Band = False
        break

if(Band):
    print("El resultado de la ecuacion es: " + str(eval(Ecu)))