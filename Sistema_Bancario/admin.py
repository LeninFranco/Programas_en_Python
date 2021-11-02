from opeSQL import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox 
from tkinter import *
from os import system
import getpass

class WAdmin:
    def __init__(self,window):
        self.window = window
        self.window.title("Banco - Admin")
        self.window.resizable(0,0)
        frame1 = LabelFrame(self.window, text="Tabla de Datos")
        frame1.grid(row=0,column=0,padx=10,pady=10)
        self.tabla = ScrolledText(frame1)
        self.tabla.config(state='disabled',width=91)
        self.tabla.grid(row=0,column=0,padx=10,pady=10)
        frame2 = LabelFrame(self.window, text="Operaciones")
        frame2.grid(row=0,column=1,padx=10,pady=10)
        Label(frame2, text="Numero de cuenta:").grid(row=0,column=0,sticky=E,padx=10,pady=10)
        Label(frame2, text="Nombre del titular:").grid(row=1,column=0,sticky=E,padx=10,pady=10)
        Label(frame2, text="Apellido del titular:").grid(row=2,column=0,sticky=E,padx=10,pady=10)
        Label(frame2, text="Contraseña:").grid(row=3,column=0,sticky=E,padx=10,pady=10)
        Label(frame2, text="Saldo: $").grid(row=4,column=0,sticky=E,padx=10,pady=10)
        self.eCuenta = StringVar()
        Entry(frame2, textvariable=self.eCuenta, validate='key', validatecommand=(self.window.register(self.isInteger),"%S")).grid(row=0,column=1,padx=10,pady=10)
        self.eNombre = StringVar()
        Entry(frame2, textvariable=self.eNombre).grid(row=1,column=1,padx=10,pady=10)
        self.eApellido = StringVar()
        Entry(frame2, textvariable=self.eApellido).grid(row=2,column=1,padx=10,pady=10)
        self.ePassword = StringVar()
        Entry(frame2, textvariable=self.ePassword).grid(row=3,column=1,padx=10,pady=10)
        self.eSaldo = StringVar()
        Entry(frame2, textvariable=self.eSaldo, validate='key', validatecommand=(self.window.register(self.isFloat),"%S")).grid(row=4,column=1,padx=10,pady=10)
        Button(frame2, text="Guardar", width=15, command=self.guardar).grid(row=5,column=0,padx=10,pady=10)
        Button(frame2, text="Eliminar", width=15, command=self.eliminar).grid(row=5,column=1,padx=10,pady=10)
        Button(frame2, text="Editar", width=15, command=self.editar).grid(row=6,column=0,padx=10,pady=10)
        Button(frame2, text="Salir", width=15, command=self.salir).grid(row=6,column=1,padx=10,pady=10)
        Button(frame2, text="Limpiar Entradas", command=self.clearEntry).grid(row=7,column=0,columnspan=2,padx=10,pady=10,sticky=W+E)
        self.updateTable()
    def salir(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            self.window.destroy()
    def updateTable(self):
        self.tabla.config(state='normal')
        self.tabla.delete('1.0',END)
        self.tabla.insert('end', '-'*91 + "\n")
        self.tabla.insert('end', "| {:<15} | {:<15} | {:<15} | {:20} | {:<10} |".format("Cuenta","Nombre","Apellido","Contraseña","Saldo") + "\n")
        self.tabla.insert('end', '-'*91 + "\n")
        for fila in Operaciones.findall():
            self.tabla.insert('end', "| {:<15} | {:<15} | {:<15} | {:20} | {:<10} |".format(fila[0],fila[1],fila[2],fila[3],fila[4]) + "\n")
            self.tabla.insert('end', '-'*91 + "\n")
        self.tabla.config(state='disabled')
    def clearEntry(self):
        self.eCuenta.set("")
        self.eNombre.set("")
        self.eApellido.set("")
        self.ePassword.set("")
        self.eSaldo.set("")
    def isEmpty(self):
        return self.eCuenta.get() == "" or self.eNombre.get() == "" or self.eApellido.get() == "" or self.ePassword.get() == "" or self.eSaldo.get() == ""
    def guardar(self):
        if not self.isEmpty():
            if Operaciones.findone(self.eCuenta.get()) == None:
                usuario = Usuario(self.eCuenta.get(),self.eNombre.get(),self.eApellido.get(),self.ePassword.get(),float(self.eSaldo.get()))
                Operaciones.create(usuario)
                messagebox.showinfo(message="Titular guardado correctamente", title="EXITO")
                self.updateTable()
            else:
                messagebox.showerror(message="El titular con esa cuenta ya existe", title="ERROR")
            self.clearEntry()
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def eliminar(self):
        if not self.eCuenta.get() == "":
            if Operaciones.findone(self.eCuenta.get()) != None:
                Operaciones.delete(self.eCuenta.get())
                messagebox.showinfo(message="Titular eliminado correctamente", title="EXITO")
                self.updateTable()
            else:
                messagebox.showerror(message="El titular con esa cuenta no existe", title="ERROR")
            self.clearEntry()
        else:
            messagebox.showwarning(message="Favor de llenar el campo 'Cuenta'", title="ADVERTENCIA")
    def editar(self):
        if not self.isEmpty():
            if Operaciones.findone(self.eCuenta.get()) != None:
                usuario = Usuario(self.eCuenta.get(),self.eNombre.get(),self.eApellido.get(),self.ePassword.get(),float(self.eSaldo.get()))
                Operaciones.update(usuario)
                messagebox.showinfo(message="Titular editado correctamente", title="EXITO")
                self.updateTable()
            else:
                messagebox.showerror(message="El titular con esa cuenta no existe", title="ERROR")
            self.clearEntry()
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def isInteger(self,char):
        return char in "0123456789"
    def isFloat(self,char):
        return char in "0123456789."


if __name__ == "__main__":
    if getpass.getpass("Contraseña: ") == 'P0L1m4s7er!':
        system('cls')
        window = Tk()
        wadmin = WAdmin(window)
        window.mainloop()