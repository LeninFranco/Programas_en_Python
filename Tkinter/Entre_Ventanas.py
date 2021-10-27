from tkinter import *

class Sesion:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.title("Inicio de Sesion")
        self.window.eval('tk::PlaceWindow . center')
        Label(self.window, text="Usuario:").grid(row=0,column=0,padx=10,pady=10,sticky=E)
        self.eUsuario = StringVar()
        Entry(self.window, textvariable=self.eUsuario).grid(row=0,column=1,padx=10,pady=10)
        Label(self.window, text="Contraseña:").grid(row=1,column=0,padx=10,pady=10,sticky= E)
        self.eContrasena = StringVar()
        Entry(self.window, textvariable=self.eContrasena, show="*").grid(row=1,column=1,padx=10,pady=10)
        Button(self.window, text="Acceder", command=self.iniciar, width=15).grid(row=2,column=0,padx=10,pady=10)
        Button(self.window, text="Salir", command=self.salir, width=15).grid(row=2,column=1,padx=10,pady=10)
        self.window.mainloop()
    def iniciar(self):
        if self.eUsuario.get() == "DarkVenom" and self.eContrasena.get() == "spiderman2099":
            self.window.destroy()
            Main()
    def salir(self):
        self.window.destroy()

class Main: 
    def __init__(self):
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.title("Principal")
        Label(self.window, text="¡Hola Mundo!").grid(row=0,column=0,padx=20,pady=10)
        Button(self.window, text="Salir", command=self.salir, width=20).grid(row=1,column=0,padx=20,pady=10)
        self.window.mainloop()
    def salir(self):
        self.window.destroy()
        Sesion()


if __name__ == "__main__":
    Sesion()