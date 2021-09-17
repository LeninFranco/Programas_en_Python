import os

Diccionario={} #Formado por Clave:Valor los cuales es de cualquier tipo de dato (int, float, string, bool, etc...)

while(True):
    os.system("cls")
    print("MENU DE OPERACIONES CON DICCIONARIOS")
    print("1. Insertar Elemento")
    print("2. Modificar Valor de un Elemento")
    print("3. Eliminar Elemento")
    print("4. Buscar Elemento por Clave")
    print("5. Mostrar el Valor de un Elemento conociendo su Clave")
    print("6. Mostrar las Claves del Diccionario")
    print("7. Mostrar los Valores del Diccionario")
    print("8. Mostrar Diccionario Completo")
    print("9. Salir")
    opc=int(input("Opcion: "))
    if(opc==1):
        clave=int(input("Ingrese la clave del Elemento: "))
        valor=str(input("Ingrese el valor del Elemento: "))
        Diccionario[clave] = valor
        print("Se ha almacenado el elemento {}:{} correctamente".format(clave,valor))
    elif(opc==2):
        clave=int(input("Ingrese la clave del Elemento: "))
        Band=(clave in Diccionario)
        if(Band==True):
            valor=str(input("Ingrese el nuevo valor del Elemento: "))
            Diccionario[clave] = valor
            print("Se ha modificado el elemento correctamente")
        else:
            print("No existe el elemento en el Diccionario")
    elif(opc==3):
        clave=int(input("Ingrese la clave del Elemento: "))
        Band=(clave in Diccionario)
        if(Band==True):
            del(Diccionario[clave])
            print("Se ha eliminado el elemento correctamente")
        else:
            print("No existe el elemento en el Diccionario")
    elif(opc==4):
        clave=int(input("Ingrese la clave del Elemento: "))
        Band=(clave in Diccionario)
        if(Band==True):
            print("Se ha encontrado el elemento correctamente")
            print("{}:{}".format(clave,Diccionario[clave]))
        else:
            print("No existe el elemento en el Diccionario")
    elif(opc==5):
        clave=int(input("Ingrese la clave del Elemento: "))
        print(Diccionario.get(clave,"No existe el elemento en el Diccionario"))
    elif(opc==6):
        print(Diccionario.keys())
    elif(opc==7):
        print(Diccionario.values())
    elif(opc==8):
        print(Diccionario)
    elif(opc==9):
        break
    else:
        continue
    os.system("Pause")


