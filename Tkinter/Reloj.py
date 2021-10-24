from tkinter import *
from time import strftime

class App:
    def __init__(self, window):
        self.window = window
        self.window.config(bg="black")
        self.window.resizable(0,0)
        self.lbHora = Label(window, fg='green', bg='black', font=('Terminal', 12))
        self.lbHora.grid(row=0,column=0,padx=10,pady=10)
        self.lbDia = StringVar()
        Label(window, textvariable=self.lbDia, fg='green', bg='black', font=('Terminal', 12)).grid(row=1,column=0,padx=10,pady=10)
        self.lbFecha = StringVar()
        Label(window, textvariable=self.lbFecha, fg='green', bg='black', font=('Terminal', 12)).grid(row=2,column=0,padx=10,pady=10)
        self.getDate()
    def getDate(self):
        Hora = strftime('%H:%M:%S')
        Dia = strftime('%A')
        Fecha = strftime('%d - %m - %y')
        self.lbHora.config(text=Hora)
        self.lbDia.set(Dia)
        self.lbFecha.set(Fecha)
        self.lbHora.after(1000, self.getDate)
        
if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()
