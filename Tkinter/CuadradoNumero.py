from tkinter import ttk
from tkinter import *

class App:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        frame = Frame(self.window)
        frame.grid(row=0,column=0)
        Label(frame,text="Ingrese un numero").grid(row=0,column=0,padx=10,pady=10)
        self.eNumero = StringVar()
        Entry(frame, textvariable=self.eNumero, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=0,column=1,padx=10,pady=10)
        Label(frame,text="Resultado").grid(row=1,column=0)
        self.eResultado = StringVar()
        Entry(frame, state="readonly", textvariable=self.eResultado).grid(row=1, column=1)
        Button(frame,text="Calcular", command=self.calcular).grid(row=2,column=0,pady=10, padx=10,columnspan=2,sticky=W+E)
    def calcular(self):
        numero = int(self.eNumero.get())
        self.eResultado.set("{:,}".format(numero**2))
    def isNumber(self,char):
        return char in "0123456789."


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()