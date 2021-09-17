import os
os.system("cls")
#Metodos de Ordenamiento para las Listas

#Metodo Burbuja
def Burbuja(Lista):
    band = True
    while band:
        band = False
        for j in range(len(Lista)-1):
            if Lista[j] > Lista[j+1]:
                aux = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = aux
                band = True

#Metodo por Inserccion
def Inserccion(Lista):
    for i in range(1, len(Lista)):
        actual = Lista[i]
        indice = i
        while indice > 0 and Lista[indice-1] > actual:
            Lista[indice] = Lista[indice-1]
            indice -= 1
        Lista[indice] = actual

#Metodo por Seleccion
def Seleccion(Lista):
    for i in range(len(Lista)-1):
        menor = i
        for j in range(i+1, len(Lista)):
            if Lista[j] < Lista[menor]:
                menor = j
        aux = Lista[menor]
        Lista[menor] = Lista[i]
        Lista[i] = aux

#Metodo Quicksort
def Partition(Lista,menor,mayor):
    pivote = Lista[menor]
    izq = menor + 1
    der = mayor
    while True:
        while izq <= der and Lista[izq] <= pivote:
            izq += 1
        while izq <= der and Lista[der] >= pivote:
            der -= 1
        if der < izq:
            break
        else:
            aux = Lista[izq]
            Lista[izq] = Lista[der]
            Lista[der] = aux
    aux = Lista[menor]
    Lista[menor] = Lista[der]
    Lista[der] = aux
    return der
def Quicksort(Lista,menor,mayor):
    if menor < mayor:
        pivote = Partition(Lista,menor,mayor)
        Quicksort(Lista,menor,pivote-1)
        Quicksort(Lista,pivote+1,mayor)

#Main
if __name__ == "__main__":
    Lista = [7,2,8,0,1,6,4,5,3,9]
    Quicksort(Lista,0,len(Lista)-1)
    print(Lista)
os.system("Pause")