def MainMenu():
    print("---------- CALCULADORA BASICA ----------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    print("----------------------------------------")
    try:
        var = int(input("> "))
        if var >= 1 and var <= 5:
            return var
        else:
            return -1
    except ValueError:
        return -1

def SubMenu():
    try:
        a = float(input("Numero 1: "))
        b = float(input("Numero 2: "))
        return a,b
    except ValueError:
        return -1