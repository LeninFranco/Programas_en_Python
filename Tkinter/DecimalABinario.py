from tkinter import *

class App:
    def __init__(self,window):
        self.window = window
        self.window.resizable(0,0)
        self.eNumero = IntVar()
        self.eNumero.set(0)
        self.eNumero.trace("w", self.convertir)
        Entry(self.window, textvariable=self.eNumero, width=20,validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=0,column=0,padx=10,pady=10)
        self.lbResultado = StringVar()
        Label(self.window, textvariable=self.lbResultado).grid(row=1,column=0,padx=10,pady=10)
    def convertir(self, *args):
        try:
            self.lbResultado.set(bin(self.eNumero.get())[2:])
        except:
            self.lbResultado.set("")
    def isNumber(self,char):
        return char in "0123456789"

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()