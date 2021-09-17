import os

#ID = XYYXX, donde las X son numeros y las Y son letras

#Clase Productos
class Producto:
    def __init__(self,ID,Nombre,Precio):
        self.ID = ID
        self.Nombre = Nombre
        self.Precio = Precio
    def __str__(self):
        return "ID: {}\nNombre: {}\nPrecio: ${}\n".format(self.ID,self.Nombre,self.Precio)

#Clase de la Tabla Hash de tamaño 20
class HashTable:
    def __init__(self):
        self.MAX = 20
        self.H = {i:[] for i in range(0,self.MAX+1)} 
    def HashFuntion(self,Producto):
        id = Producto.ID
        return ord(id[1])%self.MAX
    def Insert(self,Producto):
        key = self.HashFuntion(Producto)
        aux = self.H[key]
        aux.append(Producto)
        self.H[key] = aux
        print("Se ha ingresado el dato correctamente")
    def Delete(self,Producto):
        key = self.HashFuntion(Producto)
        aux = self.H[key]
        band = False
        ind = 0
        if not aux:
            print("No se ha encontrado el valor a eliminar")
        else:
            for i in aux:
                if(i.ID == Producto.ID):
                    band = True
                    break
                ind += 1
            if(band):
                aux.pop(ind)
                print("Se ha eliminado el dato correctamente")
            else:
                print("No se ha a encontrado el valor a eliminar")
    def Search(self,Producto):
        key = self.HashFuntion(Producto)
        aux = self.H[key]
        band = False
        ind = 0
        if not aux:
            print("No se ha encontrado el valor a buscar")
        else:
            for i in aux:
                if(i.ID == Producto.ID):
                    band = True
                    break
                ind += 1
            if(band):
                print("Se ha encontrado el valor correctamente")
                print(aux[ind])
            else:
                print("No se ha a encontrado el valor a buscar")
    def ShowData(self):
        for key, value in self.H.items():
            if not value:
                continue
            for i in value:
                print(f"Hash Key: {key}")
                print(i)

#Funciones
def Menu():
    os.system("cls")
    print("*********IMPLEMENTACION TABLA HASH*********")
    print("1. Insertar un Producto")
    print("2. Eliminar un Producto")
    print("3. Buscar un Producto")
    print("4. Mostrar solo los Datos")
    print("5. Salir")
    opc = int(input(">>> "))
    return opc
#Main
H = HashTable()
while True:
    opc = Menu()
    if(opc == 1):
        ID = input("Ingrese el ID del producto: ")
        Nombre = input("Ingrese el nombre del producto: ")
        Precio = float(input("Ingrese el precio del producto: "))
        H.Insert(Producto(ID,Nombre,Precio))
    elif(opc == 2):
        ID = input("Ingrese el ID del producto a eliminar: ")
        H.Delete(Producto(ID," ",0))
    elif(opc == 3):
        ID = input("Ingrese el ID del producto a buscar: ")
        H.Delete(Producto(ID," ",0))
    elif(opc == 4):
        H.ShowData()
    elif(opc == 5):
        break
    else:
        continue
    os.system("Pause")
os.system("Pause")