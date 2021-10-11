#Requiere la siguiente libreria
#1. pip install requests

import requests
import os
import time
import tkinter as tk

class App:
    def __init__(self, root):
        root.title("Michis")
        width=156
        height=87
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Boton=tk.Button(root)
        Boton["bg"] = "#efefef"
        Boton["fg"] = "#000000"
        Boton["justify"] = "center"
        Boton["text"] = "Cambiar"
        Boton.place(x=40,y=30,width=70,height=25)
        Boton["command"] = self.Boton_command

    def Boton_command(self):
        os.system("taskkill /IM ImageGlass.exe /F") #Cierra el programa visualizador de imagenes por defecto en tu PC. Especificar el .exe.
        michi = requests.get('http://thecatapi.com/api/images/get?format=src&type=gif')
        file = open("michi.gif","wb")
        file.write(michi.content)
        file.close()
        os.startfile(r"michi.gif") #Abre el archivo .gif creado con tu programa visualizador de imagenes por defecto. 

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
