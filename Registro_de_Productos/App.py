from tkinter import *
from tkinter import messagebox
from Row_Data import *
from Info import *
import sqlite3

#Funcion de Excepcion de entrada de datos no flotantes
def float_test(var):
    try:
        float(var)
        return True
    except:
        return False

#Funcion de Excepcion de entrada de datos no enteros
def integer_test(var):
    try:
        int(var)
        return True
    except:
        return False

#-------------------------Funciones-------------------------
def ConexionBBDD():
    try:
        conection = sqlite3.connect("Productos.db")
        conection.execute('''CREATE TABLE DATOSPRODUCTOS(ID INTEGER PRIMARY KEY, N_PRODUCTO VARCHAR(50), C_NETO REAL, CANTIDAD INTEGER, PRECIO REAL)''')
        conection.commit()
        messagebox.showinfo("BBDD", "La BBDD ha sido creada exitosamente")
    except:
        messagebox.showerror("BBDD", "La BBDD ya existe")

def SalirApp():
    valor=messagebox.askquestion("Salir","¿Desea salir de la aplicacion?")
    if valor == "yes":
        root.destroy()

def LimpiarCampos():
    Id.set("")
    Producto.set("")
    Neto.set("")
    Cantidad.set("")
    Precio.set("")

def AcercaDe():
    messagebox.showinfo("Acerca de la Aplicacion", "Version: 1.0\nDesarrollador: Lenin Franco\nEscuela Superior de Computo(IPN)")

def Insertar():
    c1 = Id.get()
    c2 = Producto.get()
    c3 = Neto.get()
    c4 = Cantidad.get()
    c5 = Precio.get()
    if integer_test(c1) and float_test(c3) and float_test(c4) and float_test(c5):
        if Buscar_Repetido(c1):
            conection = sqlite3.connect("Productos.db")
            conection.execute('''INSERT INTO DATOSPRODUCTOS(ID,N_PRODUCTO,C_NETO,CANTIDAD,PRECIO) VALUES(?,?,?,?,?)''',(int(c1),c2,float(c3),float(c4),float(c5)))
            conection.commit()
            messagebox.showinfo("BBDD", "Registro guardado correctamente")
            LimpiarCampos()
        else:
            messagebox.showinfo("BBDD", f"Ya existe un producto con la ID: {c1}")
            LimpiarCampos()
    else:
        messagebox.showerror("¡ERROR!","Uno de los campos tiene datos no validos\nVuelva a intentar")
        LimpiarCampos()

def Buscar_Repetido(c1):
    conection = sqlite3.connect("Productos.db")
    cursor = conection.execute('''SELECT * FROM DATOSPRODUCTOS WHERE ID=?''',(int(c1),))
    fila = cursor.fetchone()
    conection.commit()
    return fila == None

def Eliminar():
    c1 = Id.get()
    if integer_test(c1):
        conection = sqlite3.connect("Productos.db")
        cursor = conection.execute('''SELECT * FROM DATOSPRODUCTOS WHERE ID=?''',(int(c1),))
        fila = cursor.fetchone()
        if fila != None:
            conection.execute('''DELETE FROM DATOSPRODUCTOS WHERE ID=?''',(int(c1),))
            messagebox.showinfo("BBDD", "El registro se ha eliminado correctamente")
        else:
            messagebox.showinfo("BBDD", "No se ha encontrado el registro a eliminar")
        conection.commit()
        LimpiarCampos()
    else:
        messagebox.showerror("¡ERROR!","Uno de los campos tiene datos no validos\nVuelva a intentar")
        LimpiarCampos()

def Buscar():
    c1 = Id.get()
    if integer_test(c1):
        conection = sqlite3.connect("Productos.db")
        cursor = conection.execute('''SELECT * FROM DATOSPRODUCTOS WHERE ID=?''',(int(c1),))
        fila = cursor.fetchone()
        if fila != None:
            Mostrar_Fila(fila)
        else:
            messagebox.showinfo("BBDD", "No se ha encontrado el registro")
        conection.commit()
        LimpiarCampos()
    else:
        messagebox.showerror("¡ERROR!","Uno de los campos tiene datos no validos\nVuelva a intentar")
        LimpiarCampos()

def Actualizar():
    c1 = Id.get()
    c2 = Producto.get()
    c3 = Neto.get()
    c4 = Cantidad.get()
    c5 = Precio.get()
    if integer_test(c1) and float_test(c3) and float_test(c4) and float_test(c5):
        if not Buscar_Repetido(c1):
            conection = sqlite3.connect("Productos.db")
            conection.execute('''UPDATE DATOSPRODUCTOS SET ID=? WHERE ID=?''',(int(c1),int(c1)))
            conection.execute('''UPDATE DATOSPRODUCTOS SET N_PRODUCTO=? WHERE ID=?''',(c2,int(c1)))
            conection.execute('''UPDATE DATOSPRODUCTOS SET C_NETO=? WHERE ID=?''',(float(c3),int(c1)))
            conection.execute('''UPDATE DATOSPRODUCTOS SET CANTIDAD=? WHERE ID=?''',(float(c4),int(c1)))
            conection.execute('''UPDATE DATOSPRODUCTOS SET PRECIO=? WHERE ID=?''',(float(c5),int(c1)))
            conection.commit()
            messagebox.showinfo("BBDD", "Registro actualizado correctamente")
            LimpiarCampos()
        else:
            messagebox.showinfo("BBDD", f"No existe un producto con la ID: {c1}")
            LimpiarCampos()
    else:
        messagebox.showerror("¡ERROR!","Uno de los campos tiene datos no validos\nVuelva a intentar")
        LimpiarCampos()

#-----------------------------------Interfaz Grafica-----------------------------------
root = Tk()
root.title("Tiendita UwU")
root.resizable(0,0)
root.iconbitmap(r'ico/Icon.ico')

#----------Menu Barra y Casacada----------
Menu_Barra = Menu(root)
root.config(menu=Menu_Barra, width=300, height = 300)

bbddMenu = Menu(Menu_Barra, tearoff=0)
bbddMenu.add_command(label="Conectar", command=ConexionBBDD)
bbddMenu.add_command(label="Salir", command=SalirApp)

Limpiar = Menu(Menu_Barra, tearoff=0)
Limpiar.add_command(label="Limpiar Campos", command=LimpiarCampos)

Ayuda = Menu(Menu_Barra, tearoff=0)
Ayuda.add_command(label="Acerca de...", command=AcercaDe)
Ayuda.add_command(label="Instrucciones", command=Instrucciones)

Menu_Barra.add_cascade(label="BBDD", menu=bbddMenu)
Menu_Barra.add_cascade(label="Limpiar", menu=Limpiar)
Menu_Barra.add_cascade(label="Ayuda", menu=Ayuda)

#----------Frame 1----------
Frame1 = Frame(root)
Frame1.pack()

Id = StringVar()
Producto = StringVar()
Neto = StringVar()
Cantidad = StringVar()
Precio = StringVar()

cuadroID = Entry(Frame1, textvariable=Id)
cuadroID.grid(row=0,column=1, padx=10, pady=10)

cuadroProducto = Entry(Frame1, textvariable=Producto)
cuadroProducto.grid(row=1,column=1, padx=10, pady=10)

cuadroNeto = Entry(Frame1, textvariable=Neto)
cuadroNeto.grid(row=2,column=1, padx=10, pady=10)

cuadroCantidad = Entry(Frame1, textvariable=Cantidad)
cuadroCantidad.grid(row=3,column=1, padx=10, pady=10)

cuadroPrecio = Entry(Frame1, textvariable=Precio)
cuadroPrecio.grid(row=4,column=1, padx=10, pady=10)

IDLabel = Label(Frame1, text="ID:")
IDLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

ProductoLabel = Label(Frame1, text="Producto:")
ProductoLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

NetoLabel = Label(Frame1, text="Contenido Neto:")
NetoLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

CantLabel = Label(Frame1, text="Cantidad:")
CantLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

PrecioLabel = Label(Frame1, text="Precio:")
PrecioLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

#----------Frame 2----------
Frame2 = Frame(root)
Frame2.pack()

botonAdd = Button(Frame2, text="Añadir", command=Insertar)
botonAdd.grid(row=1, column=0, sticky="e", padx=10,pady=10)

botonBuscar = Button(Frame2, text="Buscar", command=Buscar)
botonBuscar.grid(row=1, column=1, sticky="e", padx=10,pady=10)

botonActualizar = Button(Frame2, text="Actualizar", command=Actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10,pady=10)

botonBorrar = Button(Frame2, text="Eliminar", command=Eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10,pady=10)

root.mainloop()