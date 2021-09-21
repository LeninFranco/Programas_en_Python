from pymsgbox import *
import json

def openFile():
    with open("datasource.json","r") as f:
        return json.load(f)

def closeFile(db):
    with open("datasource.json","w") as f:
        json.dump(db,f,indent=4)

def isNumber(var):
    try:
        int(var)
        return True
    except:
        return False

def create():
    db = openFile()
    no = prompt("Ingrese el ID de la fritura","Create")
    if no == None:
        closeFile(db)
        alert("Proceso Cancelado","Create")
        return 
    if not isNumber(no):
        closeFile(db)
        alert("La ID debe ser un valor numerico","Create")
        return
    if no in db["Papitas"].keys():
        closeFile(db)
        alert("Ya existe un registro con la misma ID","Create")
        return 
    nombre = prompt("Ingrese el nombre de la fritura","Create")
    if nombre == None:
        closeFile(db)
        alert("Proceso Cancelado","Create")
        return 
    marca = prompt("Ingrese la marca de la fritura","Create")
    if marca == None:
        closeFile(db)
        alert("Proceso Cancelado","Create")
        return 
    precio = prompt("Ingrese el precio unitario de la fritura","Create")
    if precio == None:
        closeFile(db)
        alert("Proceso Cancelado","Create")
        return 
    cantidad = prompt("Ingrese la cantidad disponible de la fritura","Create")
    if cantidad == None:
        closeFile(db)
        alert("Proceso Cancelado","Create")
        return 
    db["Papitas"][no] = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "cantidad": cantidad
    }
    closeFile(db)
    alert("Registro Guardado Correctamente","Create")

def read():
    db = openFile()
    no = prompt("Ingrese el ID de la fritura","Read")
    if no == None:
        closeFile(db)
        alert("Proceso Cancelado","Read")
        return 
    if not isNumber(no):
        closeFile(db)
        alert("La ID debe ser un valor numerico","Read")
        return
    if no in db["Papitas"].keys():
        var = "ID: " + no + "\nNombre: " + db["Papitas"][no]["nombre"] + "\nMarca: " + db["Papitas"][no]["marca"] + "\nPrecio: $" + db["Papitas"][no]["precio"] + "\nCantidad: " + db["Papitas"][no]["cantidad"]
        alert(var,"Read")
    else:
        alert("No Se Encontro El Registro", "Read")
    closeFile(db)

def update():
    db = openFile()
    no = prompt("Ingrese el ID de la fritura","Update")
    if no == None:
        closeFile(db)
        alert("Proceso Cancelado","Update")
        return 
    if not isNumber(no):
        closeFile(db)
        alert("La ID debe ser un valor numerico","Update")
        return
    if not no in db["Papitas"].keys():
        closeFile(db)
        alert("No existe un registro con la ID que tipeo","Update")
        return
    nombre = prompt("Ingrese el nuevo nombre de la fritura \nValor Actual: " + db["Papitas"][no]["nombre"],"Update",db["Papitas"][no]["nombre"])
    if nombre == None:
        closeFile(db)
        alert("Proceso Cancelado","Update")
        return 
    marca = prompt("Ingrese la nueva marca de la fritura \nValor Actual: " + db["Papitas"][no]["marca"],"Update",db["Papitas"][no]["marca"])
    if marca == None:
        closeFile(db)
        alert("Proceso Cancelado","Update")
        return 
    precio = prompt("Ingrese el nuevo precio unitario de la fritura \nValor Actual: " + db["Papitas"][no]["precio"],"Update",db["Papitas"][no]["precio"])
    if precio == None:
        closeFile(db)
        alert("Proceso Cancelado","Update")
        return 
    cantidad = prompt("Ingrese la nueva cantidad disponible de la fritura \nValor Actual: " + db["Papitas"][no]["cantidad"],"Update",db["Papitas"][no]["cantidad"])
    if cantidad == None:
        closeFile(db)
        alert("Proceso Cancelado","Update")
        return 
    db["Papitas"][no] = {
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "cantidad": cantidad
    }
    closeFile(db)
    alert("Registro Actualizado Correctamente","Update")

def delete():
    db = openFile()
    no = prompt("Ingrese el ID de la fritura","Delete")
    if no == None:
        closeFile(db)
        alert("Proceso Cancelado","Delete")
        return 
    if not isNumber(no):
        closeFile(db)
        alert("La ID debe ser un valor numerico","Delete")
        return
    if no in db["Papitas"].keys():
        del(db["Papitas"][no])
        alert("Se Elimino El Registro Correctamente","Delete")
    else:
        alert("No Se Encontro El Registro", "Delete")
    closeFile(db)

if __name__ == "__main__":
    contrasena = password("Ingrese la contraseña: ","Inicio")
    if contrasena == "P0L1m4s7er":
        while True:
            opc = confirm("Registro de Frituras\n Favor de seleccionar una de las siguientes operaciones","CRUD Frituras",["Create","Read","Update","Delete","Salir"])
            if opc == "Create":
                create()
            elif opc == "Read":
                read()
            elif opc == "Update":
                update()
            elif opc == "Delete":
                delete()
            elif opc == "Salir":
                alert("Gracias por usarme UwU","Bye Bye")
                break
    else:
        alert("Contraseña Incorrecta","Error")