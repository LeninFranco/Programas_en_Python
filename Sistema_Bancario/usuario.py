from opeSQL import *
from tkinter import messagebox 
from tkinter import *

class SesionWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Banco - Iniciar Sesion")
        self.window.resizable(0,0)
        Label(self.window, text="Numero de cuenta:").grid(row=0,column=0,padx=10,pady=10,sticky=E)
        Label(self.window, text="Contraseña:").grid(row=1,column=0,padx=10,pady=10,sticky=E)
        self.eCuenta = StringVar()
        Entry(self.window, textvariable=self.eCuenta, validate='key', validatecommand=(self.window.register(self.isInteger),"%S")).grid(row=0,column=1,padx=10,pady=10)
        self.ePassword = StringVar()
        Entry(self.window, textvariable=self.ePassword, show="*").grid(row=1,column=1,padx=10,pady=10)
        Button(self.window, text="Iniciar Sesion", width=18, command=self.iniciar).grid(row=2,column=0,padx=10,pady=10)
        Button(self.window, text="Salir", width=18, command=self.salir).grid(row=2,column=1,padx=10,pady=10)
    def salir(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            self.window.destroy()
    def iniciar(self):
        if self.eCuenta.get() != "" and self.ePassword.get() != "":
            if Operaciones.findone(self.eCuenta.get()) != None:
                user = Operaciones.findone(self.eCuenta.get())
                if user[3] == self.ePassword.get():
                    self.window.destroy()
                    window = Tk()
                    main = MainWindow(window, Usuario(user[0],user[1],user[2],user[3],user[4]))
                    window.mainloop()
                else:
                    messagebox.showerror(message="Contraseña incorrecta", title="ERROR")
            else:
                messagebox.showerror(message="El titular con esa cuenta no existe", title="ERROR")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def isInteger(self,char):
        return char in "0123456789"

class MainWindow:
    def __init__(self, window, user):
        self.window = window
        self.user = user
        self.window.title("Banco - Principal")
        self.window.resizable(0,0)

        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        Label(frame1, text="Bienvenido " + self.user.nombre).grid(row=0,column=0,padx=10,pady=10)
        self.eSaldo = StringVar()
        self.eSaldo.set("Saldo actual: $" + str(self.user.saldo))
        Label(frame1,textvariable=self.eSaldo).grid(row=1,column=0,padx=10,pady=10)

        frame2 = LabelFrame(self.window)
        frame2.grid(row=1,column=0,padx=10,pady=10)
        self.eCantidad = StringVar()
        Entry(frame2, textvariable=self.eCantidad, validate='key', validatecommand=(self.window.register(self.isFloat),"%S"), width=40).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
        Button(frame2, text="Depositar", width=15, command=self.depositar).grid(row=1,column=0,padx=10,pady=10)
        Button(frame2, text="Retirar", width=15, command=self.retirar).grid(row=1,column=1,padx=10,pady=10)
        Button(frame2, text="Enviar Dinero", width=34, command=self.enviar).grid(row=2,column=0,padx=10,pady=10,columnspan=2)
        Button(frame2, text="Salir", width=34, command=self.salir).grid(row=3,column=0,padx=10,pady=10,columnspan=2)
    def enviar(self):
        window = Tk()
        enviar = SendWindow(window,self.user,self.eSaldo)
        window.mainloop()
    def depositar(self):
        if self.eCantidad.get() != "":
            self.user.saldo += float(self.eCantidad.get())
            self.eSaldo.set("Saldo actual: $" + str(self.user.saldo))
            self.eCantidad.set("")
            messagebox.showinfo(message="Dinero depositado correctamente", title="OPERACION EXITOSA")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def retirar(self):
        if self.eCantidad.get() != "":
            if float(self.eCantidad.get()) < self.user.saldo:
                self.user.saldo -= float(self.eCantidad.get())
                self.eSaldo.set("Saldo actual: $" + str(self.user.saldo))
                self.eCantidad.set("")
                messagebox.showinfo(message="Dinero retirado correctamente", title="OPERACION EXITOSA")
            else:
                messagebox.showerror(message="No se puede retirar cantidades mayores a la actual", title="ERROR")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def salir(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            Operaciones.update(self.user)
            self.window.destroy()
            window = Tk()
            sesion = SesionWindow(window)
            window.mainloop()
    def isFloat(self,char):
        return char in "0123456789."

class SendWindow:
    def __init__(self,window,user,saldo):
        self.window = window
        self.user = user
        self.eSaldo = saldo
        self.window.title("Banco - Enviar")
        self.window.resizable(0,0)
        Label(self.window, text="Numero de cuenta:").grid(row=0,column=0,padx=10,pady=10,sticky=E)
        Label(self.window, text="Cantidad:").grid(row=1,column=0,padx=10,pady=10,sticky=E)
        self.Cuenta = StringVar(self.window)
        Entry(self.window,textvariable=self.Cuenta,validate='key', validatecommand=(self.window.register(self.isInteger),"%S")).grid(row=0,column=1,padx=10,pady=10)
        self.Cantidad = StringVar(self.window)
        Entry(self.window,textvariable=self.Cantidad,validate='key', validatecommand=(self.window.register(self.isFloat),"%S")).grid(row=1,column=1,padx=10,pady=10)
        Button(self.window, text="Enviar", width=36, command=self.enviar).grid(row=2,column=0,padx=10,pady=10,columnspan=2)
    def enviar(self):
        if self.Cuenta.get() != "" and self.Cantidad.get() != "":
            if Operaciones.findone(self.Cuenta.get()) != None:
                user = Operaciones.findone(self.Cuenta.get())
                destino = Usuario(user[0],user[1],user[2],user[3],user[4])
                if float(self.Cantidad.get()) < self.user.saldo:
                    self.user.saldo -= float(self.Cantidad.get())
                    destino.saldo += float(self.Cantidad.get())
                    Operaciones.update(destino)
                    self.Cuenta.set("")
                    self.Cantidad.set("")
                    self.eSaldo.set("Saldo actual: $" + str(self.user.saldo))
                    messagebox.showinfo(message="Dinero enviado correctamente", title="OPERACION EXITOSA")
                else:
                    messagebox.showerror(message="No se puede enviar cantidades mayores a la actual", title="ERROR")
            else:
                messagebox.showerror(message="El titular con esa cuenta no existe", title="ERROR")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def isInteger(self,char):
        return char in "0123456789"
    def isFloat(self,char):
        return char in "0123456789."

if __name__ == "__main__":
    window = Tk()
    sesion = SesionWindow(window)
    window.mainloop()