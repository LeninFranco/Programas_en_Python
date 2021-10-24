from tkinter import ttk
from tkinter import *

class App:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        lbSaludo = Label(self.window, text="¡Hola Mundo!").grid(row=0,column=0,padx=50,pady=50)


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()