import os

Lista=[] #Puede recibir cualquier tipo de dato (int, float, string, bool, etc...)

while(True):
    os.system("cls")
    print("MENU DE OPERACIONES CON LISTAS")
    print("1. Insertar Elemento al final")
    print("2. Insertar Elemento en una posicion")
    print("3. Eliminar un Elemento por su valor ")
    print("4. Eliminar un Elemento por su indice")
    print("5. Buscar Elemento")
    print("6. Mostrar Lista completa")
    print("7. Mostrar el Primer Elemento")
    print("8. Mostrar el Ultimo Elemento")
    print("9. Mostrar Elementos de un rango")
    print("10. Numero de Elementos")
    print("11. Ordenar Elementos")
    print("12. Salir")
    opc=input("Opcion: ")
    if(opc=="1"):
        Elem=input("Ingrese el elemento: ")
        Lista.append(Elem)
        print("Se ha insertado el elemento {} correctamente".format(Elem))
    elif(opc=="2"):
        Elem=input("Ingrese el elemento: ")
        Ind=int(input("Ingrese el indice o posicion: "))
        Lista.insert(Ind,Elem)
        print("Se ha insertado el elemento {} correctamente".format(Elem))
    elif(opc=="3"):
        Elem=input("Ingrese el elemento: ")
        Band=(Elem in Lista)
        if(Band==True):
            Lista.remove(Elem)
            print("Se ha eliminado el elemento {} correctamente".format(Elem))
        else:
            print("El elemento {} no esta en la lista".format(Elem))
    elif(opc=="4"):
        Ind=int(input("Ingrese el indice: "))
        if(Ind < len(Lista)):
            aux = Lista[Ind]
            Lista.pop(Ind)
            print("Se ha eliminado el elemnto {} correctamente".format(aux))
        else:
            print("No existe un valo que ocupe el indice {}".format(Ind))
    elif(opc=="5"):
        Elem=input("Ingrese el elemento: ")
        Band=(Elem in Lista)
        if(Band==True):
            print("Se encontro el elemento {} en la lista".format(Elem))
        else:
            print("El elemento {} no esta en la lista".format(Elem))
    elif(opc=="6"):
        print(Lista[:])
    elif(opc=="7"):
        print(Lista[0])
    elif(opc=="8"):
        Ind = len(Lista) - 1 
        print(Lista[Ind])
    elif(opc=="9"):
        Prim=int(input("Ingrese el primer indice: "))
        Ultm=int(input("Ingrese el segundo indice: "))
        print(Lista[Prim:Ultm])
    elif(opc=="10"):
        print(len(Lista))
    elif(opc=="11"):
        print("Menor a Mayor")
        Lista.sort(reverse=False)
        print(Lista)
        print("Mayor a Menor")
        Lista.sort(reverse=True)
        print(Lista)
    elif(opc=="12"):
        break
    else:
        continue
    os.system("Pause")