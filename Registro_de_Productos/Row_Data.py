from tkinter import *
from tkinter import messagebox

def Mostrar_Fila(fila):
    window = Tk()
    window.title("")
    window.resizable(0,0)
    window.iconbitmap(r'ico/Icon.ico')
    Frame1 = Frame(window)
    Frame1.pack()
    cuadroID1 = Label(Frame1, text=str(fila[0]))
    cuadroID1.grid(row=0,column=1, padx=10, pady=10)
    cuadroProducto1 = Label(Frame1, text=str(fila[1]))
    cuadroProducto1.grid(row=1,column=1, padx=10, pady=10)
    cuadroNeto1 = Label(Frame1, text=str(fila[2]))
    cuadroNeto1.grid(row=2,column=1, padx=10, pady=10)
    cuadroCantidad1 = Label(Frame1, text=str(fila[3]))
    cuadroCantidad1.grid(row=3,column=1, padx=10, pady=10)
    cuadroPrecio1 = Label(Frame1, text=str(fila[4]))
    cuadroPrecio1.grid(row=4,column=1, padx=10, pady=10)
    IDLabel1 = Label(Frame1, text="ID:")
    IDLabel1.grid(row=0,column=0, sticky="e", padx=10, pady=10)
    ProductoLabel1 = Label(Frame1, text="Producto:")
    ProductoLabel1.grid(row=1,column=0, sticky="e", padx=10, pady=10)
    NetoLabel1 = Label(Frame1, text="Contenido Neto:")
    NetoLabel1.grid(row=2,column=0, sticky="e", padx=10, pady=10)
    CantLabel1 = Label(Frame1, text="Cantidad:")
    CantLabel1.grid(row=3,column=0, sticky="e", padx=10, pady=10)
    PrecioLabel1 = Label(Frame1, text="Precio: $")
    PrecioLabel1.grid(row=4,column=0, sticky="e", padx=10, pady=10)
    window.mainloop()