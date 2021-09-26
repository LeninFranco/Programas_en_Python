from os import system
from fractions import Fraction
import re

def isInteger(var):
    try:
        int(var)
        return True
    except:
        return False

def isFraction(f):
    try:
        Fraction(f)
        return True
    except:
        return False

def menu():
    print("**********Operaciones de Fracciones**********")
    print("* 1. Suma                                   *")
    print("* 2. Resta                                  *")
    print("* 3. Multiplicacion                         *")
    print("* 4. Division                               *")
    print("* 5. Salir                                  *")
    print("*********************************************")
    opc = input("Opcion -> ")
    if isInteger(opc):
        if int(opc) > 0 and int(opc) < 6:
            return int(opc)
    return -1

while True:
    system("cls")
    opc = menu()
    if opc == -1:
        continue
    elif opc == 5:
        print("\nGracias por Usarme UwU")
        break
    elif opc == 1:
        f1 = input("\nIngrese la primera fraccion (formato a/b): ")
        if not isFraction(f1):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f2 = input("\nIngrese la segunda fraccion (formato a/b): ")
        if not isFraction(f2):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f1 = Fraction(f1)
        f2 = Fraction(f2)
        print(f"\nEl resultado de {f1} + {f2} es {f1+f2}")
        print("\nNota: Las Fracciones se simplificaron automaticamente")
    elif opc == 2:
        f1 = input("\nIngrese la primera fraccion (formato a/b): ")
        if not isFraction(f1):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f2 = input("\nIngrese la segunda fraccion (formato a/b): ")
        if not isFraction(f2):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f1 = Fraction(f1)
        f2 = Fraction(f2)
        print(f"\nEl resultado de {f1} - {f2} es {f1-f2}")
        print("\nNota: Las Fracciones se simplificaron automaticamente")
    elif opc == 3:
        f1 = input("\nIngrese la primera fraccion (formato a/b): ")
        if not isFraction(f1):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f2 = input("\nIngrese la segunda fraccion (formato a/b): ")
        if not isFraction(f2):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f1 = Fraction(f1)
        f2 = Fraction(f2)
        print(f"\nEl resultado de {f1} X {f2} es {f1*f2}")
        print("\nNota: Las Fracciones se simplificaron automaticamente")
    elif opc == 4:
        f1 = input("\nIngrese la primera fraccion (formato a/b): ")
        if not isFraction(f1):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f2 = input("\nIngrese la segunda fraccion (formato a/b): ")
        if not isFraction(f2):
            print("\nEntrada no Valida")
            system("pause")
            continue
        f1 = Fraction(f1)
        f2 = Fraction(f2)
        print(f"\nEl resultado de {f1} / {f2} es {f1/f2}")
        print("\nNota: Las Fracciones se simplificaron automaticamente")
    system("pause")