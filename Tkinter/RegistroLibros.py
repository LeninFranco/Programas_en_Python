from tkinter import *
import tkinter.scrolledtext

class Libro:
    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setAutor(self,autor):
        self.autor = autor
    def getAutor(self):
        return self.autor
    def setPaginas(self,paginas):
        self.paginas = paginas
    def getPaginas(self):
        return self.paginas

class App:
    def __init__(self,window):
        self.window = window
        self.window.resizable(0,0)
        self.window.title("Registro de Libros")
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        Label(frame1, text="Nombre del libro:").grid(row=0,column=0,padx=10,pady=10)
        self.eNombre = StringVar()
        Entry(frame1, textvariable=self.eNombre).grid(row=0,column=1,padx=10,pady=10)
        Label(frame1, text="Nombre del autor:").grid(row=1,column=0,padx=10,pady=10)
        self.eAutor = StringVar()
        Entry(frame1, textvariable=self.eAutor).grid(row=1,column=1,padx=10,pady=10)
        Label(frame1, text="Numero de paginas:").grid(row=2,column=0,padx=10,pady=10)
        self.ePaginas = StringVar()
        Entry(frame1, textvariable=self.ePaginas).grid(row=2,column=1,padx=10,pady=10)
        Button(frame1, text="Guardar", command=self.guardar).grid(row=3,column=0,columnspan=2,sticky=W+E,padx=10,pady=10)
        frame2 = LabelFrame(self.window)
        frame2.grid(row=1,column=0,padx=10,pady=10)
        self.data = tkinter.scrolledtext.ScrolledText(frame2)
        self.data.grid(row=0,column=0)
        self.data.insert('end', "{:<33} | {:<33} | {:<8}".format("Libro","Autor","Paginas") + "\n")
        self.data.insert('end',"-"*80 + "\n")
        self.data.config(state='disabled')
        Button(frame2, text="Limpiar", command=self.limpiar).grid(row=1,column=0,sticky=W+E,padx=10,pady=10)
    def guardar(self):
        libro = Libro()
        libro.setNombre(self.eNombre.get())
        libro.setAutor(self.eAutor.get())
        libro.setPaginas(self.ePaginas.get())
        self.data.config(state='normal')
        fila = "{:<33} | {:<33} | {:<8}".format(libro.getNombre(),libro.getAutor(),libro.getPaginas())
        self.data.insert('end', fila + "\n")
        self.data.insert('end',"-"*80 + "\n")
        self.data.config(state='disabled')
        self.eNombre.set("")
        self.eAutor.set("")
        self.ePaginas.set("")
    def limpiar(self):
        self.data.config(state='normal')
        self.data.delete('1.0', 'end')
        self.data.insert('end', "{:<33} | {:<33} | {:<8}".format("Libro","Autor","Paginas") + "\n")
        self.data.insert('end',"-"*80 + "\n")
        self.data.config(state='disabled')

if __name__ == "__main__":
    window = Tk()
    app = App(window)
    window.mainloop()