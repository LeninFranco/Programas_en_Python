from tkinter import *

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

class App:
    def __init__(self,window):
        self.window = window
        self.window.resizable(0,0)
        Label(self.window, text="N").grid(row=0,column=0,padx=5,pady=10)
        self.eN = StringVar()
        Entry(self.window, textvariable=self.eN, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=0,column=1,padx=5,pady=10)
        Label(self.window, text="Factorial(N)").grid(row=0,column=2,padx=5,pady=10)
        self.eR = StringVar()
        Entry(self.window, textvariable=self.eR, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=0,column=3,padx=5,pady=10)
        Button(self.window, text="Calcular", command=self.calcular).grid(row=0,column=4,padx=5,pady=10)
    def calcular(self):
        r = factorial(int(self.eN.get()))
        self.eR.set(str(r))
    def isNumber(self,char):
        return char in "0123456789."


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
        
