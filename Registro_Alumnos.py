from os import system

data = {}

class Alumno:
    def __init__(self,Nombre,Apellido,Promedio):
        self.nombre = Nombre
        self.apellido = Apellido
        self.promedio = Promedio

class CRUD:
    @staticmethod
    def create(ID):
        if not ID in data.keys():
            nombre = input(" Nombre: ")
            apellido = input(" Apellido: ")
            promedio = input(" Promedio: ")
            data[ID] = Alumno(nombre,apellido,promedio)
            print(" Registro guardado correctamente")
        else:
            print(" Ya existe el registro")

    @staticmethod
    def read(ID):
        if ID in data.keys():
            print("{:<5} | {:<15} | {:<15} | {:<10}".format("ID","Nombre", "Apellido", "Promedio"))
            print("-"*60)
            print("{:<5} | {:<15} | {:<15} | {:<10}".format(ID,data[ID].nombre, data[ID].apellido, data[ID].promedio))
            print("-"*60)
        else:
            print(" No se encontro el registro")

    @staticmethod
    def update(ID):
        if ID in data.keys():
            nombre = input(" Nombre (Valor actual: {}): ".format(data[ID].nombre))
            apellido = input(" Apellido (Valor actual: {}): ".format(data[ID].apellido))
            promedio = input(" Promedio (Valor actual: {}): ".format(data[ID].promedio))
            data[ID] = Alumno(nombre,apellido,promedio)
            print(" Registro actualizado correctamente")
        else:
            print(" No se encontro el registro")

    @staticmethod
    def delete(ID):
        if ID in data.keys():
            del(data[ID])
            print(" Registro Eliminado")
        else:
            print(" No se encontro el registro")

    @staticmethod
    def printAll():
        print("{:<5} | {:<15} | {:<15} | {:<10}".format("ID","Nombre", "Apellido", "Promedio"))
        print("-"*60)
        for key in sorted(data.keys()):
            print("{:<5} | {:<15} | {:<15} | {:<10}".format(key, data[key].nombre, data[key].apellido, data[key].promedio))
            print("-"*60)

def Menu():
    print("***************************")
    print("*   REGISTRO DE ALUMNOS   *")
    print("***************************")
    print("* 1. Registrar Alumno     *")
    print("* 2. Buscar    Alumno     *")
    print("* 3. Modificar Alumno     *")
    print("* 4. Eliminar  Alumno     *")
    print("* 5. Ver todo el registro *")
    print("* 6. Salir                *")
    print("***************************")
    opc = input("\n >>> ")
    try:
        if int(opc) > 0 and int(opc) < 7:
            return int(opc)
        return -1
    except:
        return -1

if __name__ == "__main__":
    while True:
        system("cls")
        opc = Menu()
        if opc == -1:
            continue
        elif opc == 6:
            print("\nADIOS")
            system("pause")
            break
        elif opc == 1:
            ID = input("\n Ingrese una ID: ")
            CRUD.create(ID)
        elif opc == 2:
            ID = input("\n Ingrese la ID del alumno: ")
            print()
            CRUD.read(ID)
        elif opc == 3:
            ID = input("\n Ingrese la ID del alumno: ")
            CRUD.update(ID)
        elif opc == 4:
            ID = input("\n Ingrese la ID del alumno: ")
            CRUD.delete(ID)
        elif opc == 5:
            print()
            CRUD.printAll()
        print()
        system("pause")
