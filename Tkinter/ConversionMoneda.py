from tkinter import ttk
from tkinter import *

class App:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        self.variableRadio = IntVar()
        self.variableRadio.set("1")
        Radiobutton(self.window, text="Peso a Dolar", variable=self.variableRadio, value=1, command=self.click).grid(row=0,column=0,pady=10,padx=5)
        Radiobutton(self.window, text="Dolar a Peso", variable=self.variableRadio, value=2, command=self.click).grid(row=0,column=1,pady=10,padx=5)
        Label(self.window, text="Valor").grid(row=1, column=0,pady=10,padx=5)
        self.eValor = StringVar()
        Entry(self.window, textvariable=self.eValor, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=1,column=1,pady=10,padx=5)
        Label(self.window, text="Resultado").grid(row=2, column=0, pady=10,padx=5)
        self.eResultado = StringVar()
        Entry(self.window, textvariable=self.eResultado, state='readonly').grid(row=2,column=1,pady=10,padx=5)
        Button(self.window, text="Calcular", command=self.calcular).grid(row=3,column=0,columnspan=2,sticky=W+E)
    def calcular(self):
        if self.variableRadio.get() == 1:
            self.eResultado.set(str(float(self.eValor.get())/20) + " USD")
        else:
            self.eResultado.set(str(float(self.eValor.get())*20) + " MXN")
    def click(self):
        self.eValor.set("")
        self.eResultado.set("")
    def isNumber(self,char):
        return char in "0123456789."


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()