#Instalar las siguientes librerias
#1. pip install PyMsgBox

import sqlite3
import tkinter.scrolledtext
from tkinter import *
from pymsgbox import *

class Book:
    def __init__(self, isbn, name, author, genre, pages):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.genre = genre
        self.pages = pages

class Main:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        self.window.title("Libreria")
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        Label(frame1,text="ISBN:").grid(row=0,column=0,padx=10,pady=10)
        self.eISBN = StringVar()
        Entry(frame1, textvariable=self.eISBN, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=0,column=1, padx=10,pady=10)
        Label(frame1,text="Libro:").grid(row=1,column=0,padx=10,pady=10)
        self.eLibro = StringVar()
        Entry(frame1, textvariable=self.eLibro).grid(row=1,column=1,padx=10,pady=10)
        Label(frame1,text="Autor:").grid(row=2,column=0,padx=10,pady=10)
        self.eAutor = StringVar()
        Entry(frame1, textvariable=self.eAutor).grid(row=2,column=1,padx=10,pady=10)
        Label(frame1,text="Genero:").grid(row=3,column=0,padx=10,pady=10)
        self.eGenero = StringVar()
        Entry(frame1, textvariable=self.eGenero).grid(row=3,column=1,padx=10,pady=10)
        Label(frame1,text="Paginas:").grid(row=4,column=0,padx=10,pady=10)
        self.ePaginas = StringVar()
        Entry(frame1, textvariable=self.ePaginas, validate='key', validatecommand=(self.window.register(self.isNumber),"%S")).grid(row=4,column=1,padx=10,pady=10)
        frame2 = LabelFrame(self.window)
        frame2.grid(row=1,column=0,padx=10,pady=10)
        Button(frame2,text="Guardar", command=self.insert).grid(row=0,column=0,columnspan=4,padx=10,pady=10, sticky=W+E)
        Button(frame2,text="Eliminar", command=self.delete).grid(row=1,column=0,padx=10,pady=10)
        Button(frame2,text="Editar", command=self.update).grid(row=1,column=1,padx=10,pady=10)
        Button(frame2,text="Buscar", command=self.readOne).grid(row=1,column=2,padx=10,pady=10)
        Button(frame2,text="Tabla", command=self.showTable).grid(row=1,column=3,padx=10,pady=10)

    def readOne(self):
        isbn = prompt("Ingrese el ISBN del libro", "Buscar")
        if isbn == None:
            alert("Proceso Cancelado", "Buscar")
            return
        if isbn == "":
            alert("Favor de ingresar el ISBN", "Buscar")
            return
        sql = sqlite3.connect("library.db")
        cursor = sql.execute('''SELECT * FROM books WHERE ISBN = ?''',(isbn,))
        fila = cursor.fetchone()
        if fila != None:
            alert(f"Libro encontrado\n\nISBN: {fila[0]}\nLibro: {fila[1]}\nAutor: {fila[2]}\nGenero: {fila[3]}\nPaginas: {fila[4]}\n", "Buscar")
        else:
            alert("No existe el libro con esa ISBN", "Buscar")
        cursor.close()
        sql.close()

    def insert(self):
        if self.entryEmpty():
            alert("Favor de llenar los campos", "Guardar")
            return
        book = Book(self.eISBN.get(),self.eLibro.get(),self.eAutor.get(),self.eGenero.get(),self.ePaginas.get())
        sql = sqlite3.connect("library.db")
        cursor = sql.execute('''SELECT * FROM books WHERE ISBN = ?''',(book.isbn,))
        fila = cursor.fetchone()
        if fila == None:
            sql.execute('''INSERT INTO books(ISBN,name,author,genre,pages) VALUES(?,?,?,?,?)''',(book.isbn, book.name, book.author, book.genre, book.pages))
            sql.commit()
            alert("Libro almacenado correctamente", "Guardar")
            self.clearEntry()
        else:
            alert("Ya existe un libro con esa ISBN", "Guardar")
        cursor.close()
        sql.close()

    def update(self):
        isbn = prompt("Ingrese el ISBN del libro", "Editar")
        if isbn == None:
            alert("Proceso Cancelado", "Editar")
            return
        if isbn == "":
            alert("Favor de ingresar el ISBN", "Editar")
            return
        sql = sqlite3.connect("library.db")
        cursor = sql.execute('''SELECT * FROM books WHERE ISBN = ?''',(isbn,))
        fila = cursor.fetchone()
        if fila != None:
            book = Book("","","","",0)
            book.name = prompt(f"Ingrese el nombre del libro\n (Original: {fila[1]})", "Editar", default=str(fila[1]))
            if book.name == None or book.name == "":
                cursor.close()
                sql.close()
                alert("Proceso Cancelado", "Editar")
                return
            book.author = prompt(f"Ingrese el nombre del autor\n (Original: {fila[2]})", "Editar", default=str(fila[2]))
            if book.author == None or book.author == "":
                cursor.close()
                sql.close()
                alert("Proceso Cancelado", "Editar")
                return
            book.genre = prompt(f"Ingrese el genero del libro\n (Original: {fila[3]})", "Editar", default=str(fila[3]))
            if book.genre == None or book.genre == "":
                cursor.close()
                sql.close()
                alert("Proceso Cancelado", "Editar")
                return
            book.pages = prompt(f"Ingrese el numero de paginas\n (Original: {fila[4]})", "Editar", default=str(fila[4]))
            if book.pages == None or book.pages == "" or (not book.pages.isdigit()):
                cursor.close()
                sql.close()
                alert("Proceso Cancelado", "Editar")
                return
            sql.execute('''UPDATE books SET name=?,author=?,genre=?,pages=? WHERE ISBN=? ''',(book.name, book.author, book.genre, int(book.pages), isbn))
            sql.commit()
            alert("Libro editado correctamente", "Editar")
        else:
            alert("No existe el libro con esa ISBN", "Editar")
        cursor.close()
        sql.close()

    def delete(self):
        isbn = prompt("Ingrese el ISBN del libro", "Eliminar")
        if isbn == None:
            alert("Proceso Cancelado", "Eliminar")
            return
        if isbn == "":
            alert("Favor de ingresar el ISBN", "Eliminar")
            return
        sql = sqlite3.connect("library.db")
        cursor = sql.execute('''SELECT * FROM books WHERE ISBN = ?''',(isbn,))
        fila = cursor.fetchone()
        if fila != None:
            sql.execute('''DELETE FROM books WHERE ISBN=? ''',(isbn,))
            sql.commit()
            alert("Libro eliminado correctamente", "Eliminar")
        else:
            alert("No existe el libro con esa ISBN", "Eliminar")
        cursor.close()
        sql.close()

    def showTable(self):
        windowT = Tk()
        table = Table(windowT)
        windowT.mainloop()

    def isNumber(self,char):
        return char in "0123456789"

    def entryEmpty(self):
        return self.eISBN.get() == "" or self.eLibro.get() == "" or self.eAutor.get() == "" or self.eGenero.get() == "" or self.ePaginas.get() == ""
    
    def clearEntry(self):
        self.eISBN.set("")
        self.eLibro.set("")
        self.eAutor.set("")
        self.eGenero.set("")
        self.ePaginas.set("")

class Table:
    def __init__(self, window):
        self.window = window
        self.window.resizable(0,0)
        self.window.title("Libreria")
        self.table = tkinter.scrolledtext.ScrolledText(self.window)
        self.table.grid(row=0,column=0,padx=10,pady=10)
        self.table.config(width=131)
        self.table.insert('end', "-"*131 + "\n")
        self.table.insert('end', "| {:<15} | {:<50} | {:<25} | {:<15} | {:<10} |".format("ISBN","Libro","Autor","Genero","Paginas") + "\n")
        self.table.insert('end', "-"*131 + "\n")
        sql = sqlite3.connect("library.db")
        cursor = sql.execute('''SELECT * FROM books''')
        filas = cursor.fetchall()
        for fila in filas:
            self.table.insert('end',"| {:<15} | {:<50} | {:<25} | {:<15} | {:<10} |".format(fila[0],fila[1],fila[2],fila[3],fila[4]) + "\n")
            self.table.insert('end', "-"*131 + "\n")
        self.table.config(state='disabled')
        cursor.close()
        sql.close()

if __name__ == "__main__":
    window = Tk()
    main = Main(window)
    window.mainloop()