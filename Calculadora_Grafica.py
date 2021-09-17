from tkinter import *

i = 0

ventana = Tk()
ventana.title("Calculadora")

#Funciones
def click(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def AC():
    e_texto.delete(0, END)
    i = 0

def result():
    ecuacion = e_texto.get()
    AC()
    resultado = eval(ecuacion)
    e_texto.insert(0, resultado)
    i = 0

#Cuadro de texto
e_texto = Entry(ventana , font = ("Calibri 20"))

e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 5)
    #font es la fuente del texto del widget 
    #row y column para ubicar el widget en un sistema de columnas y filas
    #columspan para determinar cuantas columnas ocupara el widget
    #padx y pady para espaciar en pixeles el widget de la ventana y otros widgets en el eje x y el eje y

#Botones
boton0 = Button(ventana, font = "Calibri 10", text = "0", width = 17, heigh = 2, command = lambda: click(0))
boton1 = Button(ventana, font = "Calibri 10", text = "1", width = 5, heigh = 2, command = lambda: click(1))
boton2 = Button(ventana, font = "Calibri 10", text = "2", width = 5, heigh = 2, command = lambda: click(2))
boton3 = Button(ventana, font = "Calibri 10", text = "3", width = 5, heigh = 2, command = lambda: click(3))
boton4 = Button(ventana, font = "Calibri 10", text = "4", width = 5, heigh = 2, command = lambda: click(4))
boton5 = Button(ventana, font = "Calibri 10", text = "5", width = 5, heigh = 2, command = lambda: click(5))
boton6 = Button(ventana, font = "Calibri 10", text = "6", width = 5, heigh = 2, command = lambda: click(6))
boton7 = Button(ventana, font = "Calibri 10", text = "7", width = 5, heigh = 2, command = lambda: click(7))
boton8 = Button(ventana, font = "Calibri 10", text = "8", width = 5, heigh = 2, command = lambda: click(8))
boton9 = Button(ventana, font = "Calibri 10", text = "9", width = 5, heigh = 2, command = lambda: click(9))
boton_borrar = Button(ventana, font = "Calibri 10", text = "AC", width = 5, heigh = 2, command = lambda: AC())
boton_parentesis1 = Button(ventana, font = "Calibri 10", text = "(", width = 5, heigh = 2, command = lambda: click("("))
boton_parentesis2 = Button(ventana, font = "Calibri 10", text = ")", width = 5, heigh = 2, command = lambda: click(")"))
boton_punto = Button(ventana, font = "Calibri 10", text = ".", width = 5, heigh = 2, command = lambda: click("."))
boton_suma = Button(ventana, font = "Calibri 10", text = "+", width = 5, heigh = 2, command = lambda: click("+"))
boton_resta = Button(ventana, font = "Calibri 10", text = "-", width = 5, heigh = 2, command = lambda: click("-"))
boton_multi = Button(ventana, font = "Calibri 10", text = "*", width = 5, heigh = 2, command = lambda: click("*"))
boton_divi = Button(ventana, font = "Calibri 10", text = "/", width = 5, heigh = 2, command = lambda: click("/"))
boton_result = Button(ventana, font = "Calibri 10", text = "=", width = 5, heigh = 2, command = lambda: result())

boton0.grid(row = 5, column = 0, columnspan = 2, pady = 5)
boton1.grid(row = 4, column = 0, pady = 5)
boton2.grid(row = 4, column = 1, pady = 5)
boton3.grid(row = 4, column = 2, pady = 5)
boton4.grid(row = 3, column = 0, pady = 5)
boton5.grid(row = 3, column = 1, pady = 5)
boton6.grid(row = 3, column = 2, pady = 5)
boton7.grid(row = 2, column = 0, pady = 5)
boton8.grid(row = 2, column = 1, pady = 5)
boton9.grid(row = 2, column = 2, pady = 5)
boton_borrar.grid(row = 1, column = 0, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, pady = 5)
boton_punto.grid(row = 5, column = 2, pady = 5)
boton_suma.grid(row = 3, column = 3, pady = 5)
boton_resta.grid(row = 4, column = 3, pady = 5)
boton_multi.grid(row = 2, column = 3, pady = 5)
boton_divi.grid(row = 1, column = 3, pady = 5)
boton_result.grid(row = 5, column = 3, pady = 5)
    #command = lambda: click() para llamar una funcion mediante la funcion
    #text es el texto que tendra el boton
    #width es el ancho del boton en pixeles y el heigh es el ancho del boton en pixeles
    #row y column para ubicar el widget en un sistema de columnas y filas
    #columspan para determinar cuantas columnas ocupara el widget
    #padx y pady para espaciar en pixeles el widget de la ventana
ventana.mainloop()