from tkinter import ttk
from tkinter import *

class App:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        Label(self.window, text="Ingrese una palabra").grid(row=0,column=0,pady=10, padx=10)
        self.ePalabra = StringVar()
        Entry(self.window, textvariable=self.ePalabra).grid(row=0,column=1,padx=10)
        self.lbSalida = StringVar()
        Label(self.window, text="", textvariable=self.lbSalida).grid(row=1,column=0, columnspan=2, pady=10, padx=10)
        Button(self.window,text="Mostrar", command=self.mostrar).grid(row=2,column=0,columnspan=2,sticky=W+E)
    def mostrar(self):
        self.lbSalida.set(self.ePalabra.get())

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()