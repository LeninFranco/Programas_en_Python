from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class MainW:
    def __init__(self,window):
        self.window = window
        self.window.title("Sistema Inventario")
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.disable_exit)
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        Button(frame1, text="Lista de Playeras", width=36, command=self.open_playerasw).grid(row=0,column=0,columnspan=2,padx=5,pady=5)
        Button(frame1, text="Entradas", width=16, command=self.open_entradasw).grid(row=1,column=0,padx=5,pady=5)
        Button(frame1, text="Salidas", width=16, command=self.open_salidasw).grid(row=1,column=1,padx=5,pady=5)
        Button(frame1, text="Salir", width=36, command=self.exit_app).grid(row=2,column=0,columnspan=2,padx=5,pady=5)
    def open_playerasw(self):
        self.window.destroy()
        playeras_window = Tk()
        pw = PlayerasW(playeras_window)
        playeras_window.mainloop()
    def open_entradasw(self):
        self.window.destroy()
        entradas_window = Tk()
        ew = EntradasW(entradas_window)
        entradas_window.mainloop()
    def open_salidasw(self):
        self.window.destroy()
        entradas_window = Tk()
        sw = SalidasW(entradas_window)
        entradas_window.mainloop()    
    def exit_app(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            self.window.destroy()
    def disable_exit(self):
        pass

class PlayerasW:
    def __init__(self,window):
        self.window = window
        self.window.title("Lista de Playeras")
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.disable_exit)
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        self.table = ttk.Treeview(frame1, columns=("#1","#2","#3","#4"))
        self.table.grid(row=0,column=0,padx=5,pady=5)
        self.table.heading("#0",text="Codigo")
        self.table.heading("#1",text="Modelo")
        self.table.heading("#2",text="Talla")
        self.table.heading("#3",text="Precio")
        self.table.heading("#4",text="Cantidad")
        self.table.column("#0",width=80, minwidth=80)
        self.table.column("#1",width=200, minwidth=200)
        self.table.column("#2",width=60, minwidth=60)
        self.table.column("#3",width=60, minwidth=60)
        self.table.column("#4",width=60, minwidth=60)
        self.scrollbar = ttk.Scrollbar(self.window)
        self.scrollbar.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,padx=10,pady=10, sticky=S+E+N)
        self.fill_table()
        frame2 = LabelFrame(self.window)
        frame2.grid(row=0,column=2,padx=10,pady=10)
        Label(frame2,text="Codigo").grid(row=0,column=0,padx=5,pady=5,sticky=E)
        self.eCodigo = Entry(frame2,width=30)
        self.eCodigo.grid(row=0,column=1,padx=5,pady=5)
        Label(frame2,text="Modelo").grid(row=1,column=0,padx=5,pady=5,sticky=E)
        self.eModelo = Entry(frame2,width=30)
        self.eModelo.grid(row=1,column=1,padx=5,pady=5)
        Label(frame2,text="Talla").grid(row=2,column=0,padx=5,pady=5,sticky=E)
        self.eTalla = ttk.Combobox(frame2,width=27)
        self.eTalla["values"] = ["S","M","L"]
        self.eTalla.grid(row=2,column=1,padx=5,pady=5)
        Label(frame2,text="Precio").grid(row=3,column=0,padx=5,pady=5,sticky=E)
        self.ePrecio = Entry(frame2,width=30)
        self.ePrecio.grid(row=3,column=1,padx=5,pady=5)
        Button(frame2,text="Añadir Playera", command=self.add, width=35).grid(row=5,column=0,columnspan=2,padx=5,pady=5)
        Button(frame2,text="Regresar", command=self.exit_app, width=35).grid(row=6,column=0,columnspan=2,padx=5,pady=5)
    def exit_app(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            self.window.destroy()
            main_window = Tk()
            mw = MainW(main_window)
            main_window.mainloop()
    def add(self):
        if self.eCodigo.get() != "" and self.eModelo.get() != "" and self.eTalla.get() != "" and self.ePrecio.get() != "":
            conn = sqlite3.connect("Inventario.db")
            cursor = conn.execute('''INSERT INTO Playeras(Codigo,Modelo,Talla,Precio,Cantidad) VALUES(?,?,?,?,?)''',(self.eCodigo.get(),self.eModelo.get(),self.eTalla.get(),float(self.ePrecio.get()),0))
            conn.commit()
            cursor.close()
            conn.close()
            self.table.delete(*self.table.get_children())
            self.fill_table()
            self.eCodigo.delete(0,END)
            self.eModelo.delete(0,END)
            self.ePrecio.delete(0,END)
            messagebox.showinfo(message="Playera agregada correctamente", title="GUARDADO")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def fill_table(self):
        conn = sqlite3.connect("Inventario.db")
        cursor = conn.execute('''SELECT * FROM Playeras''')
        playeras = cursor.fetchall()
        for playera in playeras:
            self.table.insert("",END,text=playera[0],values=(playera[1],playera[2],playera[3],playera[4]))
        cursor.close()
        conn.close()
    def disable_exit(self):
        pass

class EntradasW:
    def __init__(self,window):
        self.window = window
        self.window.title("Lista de Playeras")
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.disable_exit)
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        self.table = ttk.Treeview(frame1, columns=("#1","#2","#3","#4","#5"))
        self.table.grid(row=0,column=0,padx=5,pady=5)
        self.table.heading("#0",text="ID")
        self.table.heading("#1",text="Fecha")
        self.table.heading("#2",text="Cantidad")
        self.table.heading("#3",text="Codigo")
        self.table.heading("#4",text="Modelo")
        self.table.heading("#5",text="Talla")
        self.table.column("#0",width=60, minwidth=60)
        self.table.column("#1",width=70, minwidth=70)
        self.table.column("#2",width=60, minwidth=60)
        self.table.column("#3",width=80, minwidth=80)
        self.table.column("#4",width=200, minwidth=200)
        self.table.column("#5",width=60, minwidth=60)
        self.scrollbar = ttk.Scrollbar(self.window)
        self.scrollbar.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,padx=10,pady=10, sticky=S+E+N)
        self.fill_table()
        frame2 = LabelFrame(self.window)
        frame2.grid(row=0,column=2,padx=10,pady=10)
        Label(frame2,text="Fecha").grid(row=0,column=0,padx=5,pady=5,sticky=E)
        self.eFecha = Entry(frame2,width=30)
        self.eFecha.grid(row=0,column=1,padx=5,pady=5)
        Label(frame2,text="Cantidad").grid(row=1,column=0,padx=5,pady=5,sticky=E)
        self.eCantidad = Entry(frame2,width=30)
        self.eCantidad.grid(row=1,column=1,padx=5,pady=5)
        Label(frame2,text="Codigo").grid(row=2,column=0,padx=5,pady=5,sticky=E)
        self.eCodigo = Entry(frame2,width=30)
        self.eCodigo.grid(row=2,column=1,padx=5,pady=5)
        Label(frame2,text="Modelo").grid(row=3,column=0,padx=5,pady=5,sticky=E)
        self.eModelo = Entry(frame2,width=30)
        self.eModelo.configure(state='readonly')
        self.eModelo.grid(row=3,column=1,padx=5,pady=5)
        Button(frame2,text="Buscar",command=self.find_one).grid(row=3,column=2,padx=5,pady=5)
        Button(frame2,text="Añadir Entrada", command=self.add, width=35).grid(row=5,column=0,columnspan=2,padx=5,pady=5)
        Button(frame2,text="Regresar", command=self.exit_app, width=35).grid(row=6,column=0,columnspan=2,padx=5,pady=5)
    def fill_table(self):
        conn = sqlite3.connect("Inventario.db")
        cursor = conn.execute('''SELECT Entradas.*, Playeras.Modelo, Playeras.Talla FROM Entradas INNER JOIN Playeras ON Entradas.Codigo = Playeras.Codigo''')
        playeras = cursor.fetchall()
        for playera in playeras:
            self.table.insert("",END,text=playera[0],values=(playera[1],playera[2],playera[3],playera[4],playera[5]))
        cursor.close()
        conn.close()
    def find_one(self):
        if self.eCodigo.get() != "":
            conn = sqlite3.connect("Inventario.db")
            cursor = conn.execute('''SELECT Modelo FROM Playeras WHERE Codigo=?''',(self.eCodigo.get(),))
            modelo = cursor.fetchone()
            if modelo != None:
                self.eModelo.configure(state='normal')
                self.eModelo.delete(0,END)
                self.eModelo.insert(0,modelo[0])
                self.eModelo.configure(state='readonly')
            else:
                messagebox.showerror(message="No se encontro la Playera", title="ERROR")
        else:
            messagebox.showwarning(message="Favor de llenar el campo Codigo", title="ADVERTENCIA")
    def add(self):
        if self.eFecha.get() != "" and self.eCantidad.get() != "" and self.eCodigo.get() != "" and self.eModelo.get() != "":
            conn = sqlite3.connect("Inventario.db")
            cursor = conn.execute('''SELECT * FROM Playeras WHERE Codigo=?''',(self.eCodigo.get(),))
            playera = cursor.fetchone()
            cursor = conn.execute('''UPDATE Playeras SET Cantidad=? WHERE Codigo=?''',(playera[4] + int(self.eCantidad.get()),self.eCodigo.get()))
            cursor = conn.execute('''INSERT INTO Entradas(Fecha,Cantidad,Codigo) VALUES(?,?,?)''',(self.eFecha.get(), int(self.eCantidad.get()), self.eCodigo.get()))
            conn.commit()
            cursor.close()
            conn.close()
            self.table.delete(*self.table.get_children())
            self.fill_table()
            self.eFecha.delete(0,END)
            self.eCantidad.delete(0,END)
            self.eCodigo.delete(0,END)
            self.eModelo.delete(0,END)
            messagebox.showinfo(message="Entrada agregada correctamente", title="GUARDADO")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def exit_app(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            self.window.destroy()
            main_window = Tk()
            mw = MainW(main_window)
            main_window.mainloop()
    def disable_exit(self):
        pass

class SalidasW:
    def __init__(self,window):
        self.window = window
        self.window.title("Lista de Playeras")
        self.window.resizable(0,0)
        self.window.protocol("WM_DELETE_WINDOW", self.disable_exit)
        frame1 = LabelFrame(self.window)
        frame1.grid(row=0,column=0,padx=10,pady=10)
        self.table = ttk.Treeview(frame1, columns=("#1","#2","#3","#4","#5"))
        self.table.grid(row=0,column=0,padx=5,pady=5)
        self.table.heading("#0",text="ID")
        self.table.heading("#1",text="Fecha")
        self.table.heading("#2",text="Cantidad")
        self.table.heading("#3",text="Codigo")
        self.table.heading("#4",text="Modelo")
        self.table.heading("#5",text="Talla")
        self.table.column("#0",width=60, minwidth=60)
        self.table.column("#1",width=70, minwidth=70)
        self.table.column("#2",width=60, minwidth=60)
        self.table.column("#3",width=80, minwidth=80)
        self.table.column("#4",width=200, minwidth=200)
        self.table.column("#5",width=60, minwidth=60)
        self.scrollbar = ttk.Scrollbar(self.window)
        self.scrollbar.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0,column=1,padx=10,pady=10, sticky=S+E+N)
        self.fill_table()
        frame2 = LabelFrame(self.window)
        frame2.grid(row=0,column=2,padx=10,pady=10)
        Label(frame2,text="Fecha").grid(row=0,column=0,padx=5,pady=5,sticky=E)
        self.eFecha = Entry(frame2,width=30)
        self.eFecha.grid(row=0,column=1,padx=5,pady=5)
        Label(frame2,text="Cantidad").grid(row=1,column=0,padx=5,pady=5,sticky=E)
        self.eCantidad = Entry(frame2,width=30)
        self.eCantidad.grid(row=1,column=1,padx=5,pady=5)
        Label(frame2,text="Codigo").grid(row=2,column=0,padx=5,pady=5,sticky=E)
        self.eCodigo = Entry(frame2,width=30)
        self.eCodigo.grid(row=2,column=1,padx=5,pady=5)
        Label(frame2,text="Modelo").grid(row=3,column=0,padx=5,pady=5,sticky=E)
        self.eModelo = Entry(frame2,width=30)
        self.eModelo.configure(state='readonly')
        self.eModelo.grid(row=3,column=1,padx=5,pady=5)
        Button(frame2,text="Buscar",command=self.find_one).grid(row=3,column=2,padx=5,pady=5)
        Button(frame2,text="Añadir Salida", command=self.add, width=35).grid(row=5,column=0,columnspan=2,padx=5,pady=5)
        Button(frame2,text="Regresar", command=self.exit_app, width=35).grid(row=6,column=0,columnspan=2,padx=5,pady=5)
    def fill_table(self):
        conn = sqlite3.connect("Inventario.db")
        cursor = conn.execute('''SELECT Salidas.*, Playeras.Modelo, Playeras.Talla FROM Salidas INNER JOIN Playeras ON Salidas.Codigo = Playeras.Codigo''')
        playeras = cursor.fetchall()
        for playera in playeras:
            self.table.insert("",END,text=playera[0],values=(playera[1],playera[2],playera[3],playera[4],playera[5]))
        cursor.close()
        conn.close()
    def find_one(self):
        if self.eCodigo.get() != "":
            conn = sqlite3.connect("Inventario.db")
            cursor = conn.execute('''SELECT Modelo FROM Playeras WHERE Codigo=?''',(self.eCodigo.get(),))
            modelo = cursor.fetchone()
            if modelo != None:
                self.eModelo.configure(state='normal')
                self.eModelo.delete(0,END)
                self.eModelo.insert(0,modelo[0])
                self.eModelo.configure(state='readonly')
            else:
                messagebox.showerror(message="No se encontro la Playera", title="ERROR")
        else:
            messagebox.showwarning(message="Favor de llenar el campo Codigo", title="ADVERTENCIA")
    def add(self):
        if self.eFecha.get() != "" and self.eCantidad.get() != "" and self.eCodigo.get() != "" and self.eModelo.get() != "":
            conn = sqlite3.connect("Inventario.db")
            cursor = conn.execute('''SELECT * FROM Playeras WHERE Codigo=?''',(self.eCodigo.get(),))
            playera = cursor.fetchone()
            cursor = conn.execute('''UPDATE Playeras SET Cantidad=? WHERE Codigo=?''',(playera[4] - int(self.eCantidad.get()),self.eCodigo.get()))
            cursor = conn.execute('''INSERT INTO Salidas(Fecha,Cantidad,Codigo) VALUES(?,?,?)''',(self.eFecha.get(), int(self.eCantidad.get()), self.eCodigo.get()))
            conn.commit()
            cursor.close()
            conn.close()
            self.table.delete(*self.table.get_children())
            self.fill_table()
            self.eFecha.delete(0,END)
            self.eCantidad.delete(0,END)
            self.eCodigo.delete(0,END)
            self.eModelo.delete(0,END)
            messagebox.showinfo(message="Salida agregada correctamente", title="GUARDADO")
        else:
            messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")
    def exit_app(self):
        if messagebox.askyesno(message="¿Desea salir de la aplicación?", title="Advertencia"):
            self.window.destroy()
            main_window = Tk()
            mw = MainW(main_window)
            main_window.mainloop()
    def disable_exit(self):
        pass

if __name__ == "__main__":
    main_window = Tk()
    mw = MainW(main_window)
    main_window.mainloop()