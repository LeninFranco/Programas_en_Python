from tkinter import *

class App:
    def __init__(self,window):
        self.window = window
        self.window.resizable(0,0)
        self.eN = IntVar()
        self.eN.set(0)
        Entry(self.window, textvariable=self.eN, state='readonly').grid(row=0,column=0,padx=5,pady=10)
        Button(self.window, text="Incrementar", command=self.incrementar).grid(row=0,column=1,padx=5,pady=10)
        Button(self.window, text="Decrementar", command=self.decrementar).grid(row=0,column=2,padx=5,pady=10)
        Button(self.window, text="Reiniciar", command=self.reiniciar).grid(row=0,column=3,padx=5,pady=10)
    def incrementar(self):
        self.eN.set(self.eN.get() + 1)
    def decrementar(self):
        self.eN.set(self.eN.get() - 1)
    def reiniciar(self):
        self.eN.set(0)

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
