from tkinter import ttk
from tkinter import *

class App:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0, padx=20,pady=5)
        Label(frame1, text="Numero 1").grid(row=0,column=0,padx=5,pady=5)
        self.eNum1 = StringVar()
        Entry(frame1, textvariable=self.eNum1, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=0,column=1,padx=5,pady=5)
        Label(frame1, text="Numero 2").grid(row=1,column=0,padx=5,pady=5)
        self.eNum2 = StringVar()
        Entry(frame1, textvariable=self.eNum2, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=1,column=1,padx=5,pady=5)
        frame2 = LabelFrame(self.window)
        frame2.grid(row=1,column=0,padx=20, pady=5)
        Button(frame2, text="Suma", command=self.suma, width=12).grid(row=0,column=0, padx=5, pady=5)
        Button(frame2, text="Resta", command=self.resta, width=12).grid(row=0,column=1, padx=5, pady=5)
        Button(frame2, text="Multiplicacion", command=self.multi, width=12).grid(row=1,column=0, padx=5, pady=5)
        Button(frame2, text="Division", command=self.divi, width=12).grid(row=1,column=1, padx=5, pady=5)
        frame3 = LabelFrame(self.window)
        frame3.grid(row=2,column=0,padx=20,pady=5)
        Label(frame3, text="Resultado").grid(row=0,column=0,padx=5,pady=5)
        self.eResultado = StringVar()
        Entry(frame3, textvariable=self.eResultado, state='readonly').grid(row=0,column=1,padx=5,pady=5)
    def suma(self):
        self.eResultado.set("{:,}".format(float(self.eNum1.get()) + float(self.eNum2.get())))
    def resta(self):
        self.eResultado.set("{:,}".format(float(self.eNum1.get()) - float(self.eNum2.get())))
    def multi(self):
        self.eResultado.set("{:,}".format(float(self.eNum1.get()) * float(self.eNum2.get())))
    def divi(self):
        self.eResultado.set("{:,}".format(float(self.eNum1.get()) / float(self.eNum2.get())))
    def isNumber(self,char):
        return char in "0123456789.-"

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()