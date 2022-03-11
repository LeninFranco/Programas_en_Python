import string
import os
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

class App:
    def __init__(self,window):
        self.window = window
        self.window.resizable(0,0)
        self.window.title("Cifrado de Corriemiento N")
        self.window.eval('tk::PlaceWindow . center')
        self.alfabeto = list(string.printable)[:95]
        self.clave = 3
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        Button(frame1, text="Cifrar Mensaje en TXT", width=50, command=self.cifrar).grid(row=0,column=0,sticky=W+E,padx=10,pady=10)
        Button(frame1, text="Descifrar Mensaje en TXT", width=50, command=self.descifrar).grid(row=1,column=0,sticky=W+E,padx=10,pady=10)
        Button(frame1, text="Modificar la clave", width=50, command=self.modificar).grid(row=2,column=0,sticky=W+E,padx=10,pady=10)
    def cifrar(self):
        ruta = fd.askopenfile(initialdir=os.getcwd(), title='Seleccione un archivo', filetype=(('txt files', "*.txt"),('all files', '*')))
        archivo = open(ruta.name, "r", encoding='utf-8')
        mensaje = archivo.read()
        archivo.close()
        mensaje_cifrado = ""
        for caracter in mensaje:
            if caracter in self.alfabeto:
                indice = self.alfabeto.index(caracter) + self.clave
                mensaje_cifrado += self.alfabeto[indice % len(self.alfabeto)]
            else: 
                mensaje_cifrado += caracter
        archivo = open('cifrado.txt','w', encoding='utf-8')
        archivo.write(mensaje_cifrado)
        archivo.close()
        mb.showinfo(title="Operación Exitosa", message="El mensaje ha sido correctamente cifrado")
    def descifrar(self):
        ruta = fd.askopenfile(initialdir=os.getcwd(), title='Seleccione un archivo', filetype=(('txt files', "*.txt"),('all files', '*')))
        archivo = open(ruta.name, "r", encoding='utf-8')
        mensaje = archivo.read()
        archivo.close()
        mensaje_descifrado = ""
        inv_clave = len(self.alfabeto) - self.clave
        for caracter in mensaje:
            if caracter in self.alfabeto:
                indice = self.alfabeto.index(caracter) + inv_clave
                mensaje_descifrado += self.alfabeto[indice % len(self.alfabeto)]
            else:
                mensaje_descifrado += caracter
        archivo = open('descifrado.txt','w', encoding='utf-8')
        archivo.write(mensaje_descifrado)
        archivo.close()
        mb.showinfo(title="Operación Exitosa", message="El mensaje ha sido correctamente descifrado")
    def modificar(self):
        win = Tk()
        win.resizable(0,0)
        win.title("Modificar Clave")
        Label(win, text="Clave").grid(row=0,column=0,padx=5,pady=10)
        self.e = Entry(win, validate='key', validatecommand=(win.register(self.isNumber),"%S"), width=25)
        self.e.grid(row=0,column=1,padx=5,pady=10)
        Button(win, text="Guardar", command=self.guardar).grid(row=0,column=2,padx=5,pady=10)
        self.l1 = Label(win, text="Clave actual: " + str(self.clave))
        self.l1.grid(row=1,column=0,columnspan=3,padx=5,pady=10, sticky=W)
        win.mainloop()
    def guardar(self):
        print(self.e.get())
        new_clave = int(self.e.get())
        mb.showinfo(title="Operación Exitosa", message="Clave Cambiado")
        self.clave = new_clave
        self.e.delete(0,END)
        self.l1['text'] = "Clave actual: " + str(self.clave)
    def isNumber(self,char):
        return char in "0123456789"


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
