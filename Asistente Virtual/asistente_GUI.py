# Instalar los siguientes paquetes para el correcto funcionamiento
# 1. pip install SpeechRecognition
# 2. pip install pyttsx3
# 3. pip install PyAudio
# 4. pip install pywhatkit

from tkinter import messagebox
from tkinter import ttk
import sqlite3
import speech_recognition as sr
import pyttsx3, pywhatkit
import subprocess as sub
import os
from datetime import datetime
from tkinter import *

#Diccionario de Meses para la consulta de fechas
months = {
    "1": "enero",
    "2": "febrero",
    "3": "marzo",
    "4": "abril",
    "5": "mayo",
    "6": "junio",
    "7": "julio",
    "8": "agosto",
    "9": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}

#Las direcciones Web deben existir (Comando "abre")
sql = sqlite3.connect("AS.db")
cursor = sql.execute('''SELECT * FROM sitios''')
filas = cursor.fetchall()
sites = {fila[0]:fila[1] for fila in filas}
sql.close()

#Las direcciones deben ser de tus archivos y programas que tengas instalados (Comando "abre")
sql = sqlite3.connect("AS.db")
cursor = sql.execute('''SELECT * FROM apps''')
filas = cursor.fetchall()
apps = {fila[0]:fila[1] for fila in filas}
sql.close()

name = "cortana"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            talk("Te escucho")
            pc = listener.listen(source, phrase_time_limit=5)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
            return rec
    except:
        return "silencio"

def run_cortana():
    while(True):
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce','')
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
            continue
        if 'abre' in rec:
            band = False
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
                    band = True
                    break
            for app in apps:
                if app in rec:
                    os.startfile(apps[app])
                    talk(f'Abriendo {app}')
                    band = True
                    break
            if(not band):
                talk("Los siento, no has agregado el sitio Web o aplicación que solicita")
            continue
        if 'busca' in rec:
            search = rec.replace('busca','')
            search = search.split()
            sub.call('start chrome.exe https://google.com/search?q='+'+'.join(search), shell=True)
            talk("Encontre estos resultados")
            continue
        if 'dime la hora' in rec:
            now = datetime.now()
            talk(f"Son las {now.hour} horas con {now.minute} minutos")
            continue
        if 'dime la fecha de hoy' in rec:
            now = datetime.now()
            talk(f"Hoy es {now.day} de {months[str(now.month)]} de {now.year}")
            continue
        if 'qué eres' in rec or 'eres' in rec:
            talk("Soy Cortana, un asistente virtual desarrollado en el lenguaje de programación Python")
            continue
        if 'gracias' in rec:
            talk("De nada")
            continue
        if 'silencio' in rec:
            talk("No te escucho, ¿en que puedo ayudarte?")
            continue
        if 'apagar' in rec or 'adiós' in rec:
            talk("Apagando, nos vemos")
            break
        talk("No te entiendo, podrias repetir tu peticion de nuevo por favor")

def add_web_window():
    global eClaveWeb, eValorWeb
    window = Tk()
    window.resizable(0,0)
    window.title("Agregar un Sitio Web")
    window.configure(bg="black")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    frame1.config(bg="black", foreground="white")
    Label(frame1,text="Nombre o Palabra Clave", bg="black", fg="white").grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
    eClaveWeb = Entry(frame1,width=50, bg="black", fg="white", insertbackground='white')
    eClaveWeb.grid(row=1,column=0,padx=5,pady=5)
    Label(frame1,text="URL del Sitio Web", bg="black", fg="white").grid(row=2,column=0,padx=5,pady=5,sticky=W+E)
    eValorWeb = Entry(frame1,width=50, bg="black", fg="white", insertbackground='white')
    eValorWeb.grid(row=3,column=0,padx=5,pady=5)
    Button(frame1,text="Agregar",command=add_web, bg="black", fg="white").grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
    window.mainloop()

def add_web():
    if eClaveWeb.get().strip() != "" or eValorWeb.get().strip() != "":
        sites[eClaveWeb.get()] = eValorWeb.get()
        sql = sqlite3.connect("AS.db")
        sql.execute('''INSERT INTO sitios(clave,url) VALUES(?,?)''',(eClaveWeb.get(),eValorWeb.get()))
        sql.commit()
        sql.close()
        messagebox.showinfo(message="Sitio Web agregado correctamente", title="OPERACION EXITOSA")
        eClaveWeb.delete(0,"end")
        eValorWeb.delete(0,"end")
    else:
        messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")

def add_app_window():
    global eClaveApp, eValorApp
    window = Tk()
    window.resizable(0,0)
    window.title("Agregar un Aplicación")
    window.configure(bg="black")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    frame1.config(bg="black", foreground="white")
    Label(frame1,text="Nombre o Palabra Clave", bg="black", fg="white").grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
    eClaveApp = Entry(frame1,width=50, bg="black", fg="white", insertbackground='white')
    eClaveApp.grid(row=1,column=0,padx=5,pady=5)
    Label(frame1,text="Ruta de la Aplicación", bg="black", fg="white").grid(row=2,column=0,padx=5,pady=5,sticky=W+E)
    eValorApp = Entry(frame1,width=50, insertbackground='white', bg="black", fg="white")
    eValorApp.grid(row=3,column=0,padx=5,pady=5)
    Button(frame1,text="Agregar",command=add_app, bg="black", fg="white").grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
    window.mainloop()

def add_app():
    if eClaveApp.get().strip() != "" or eValorApp.get().strip() != "":
        direccion = eValorApp.get().strip()
        direccion = direccion.rsplit("\n")
        apps[eClaveApp.get()] = direccion[0]
        sql = sqlite3.connect("AS.db")
        sql.execute('''INSERT INTO apps(clave,ruta) VALUES(?,?)''',(eClaveApp.get(),direccion[0]))
        sql.commit()
        sql.close()
        messagebox.showinfo(message="Aplicacion agregada correctamente", title="OPERACION EXITOSA")
        eClaveApp.delete(0,"end")
        eValorApp.delete(0,"end")
    else:
        messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")

def show_web():
    window = Tk()
    window.resizable(0,0)
    window.title("Sitios Web")
    window.configure(bg="black")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    frame1.config(bg="black", foreground="white")
    tabla = ttk.Treeview(frame1,columns=2)
    tabla.grid(row=0,column=0,padx=5,pady=5,columnspan=2)
    tabla.heading("#0", text="Clave o Nombre")
    tabla.heading("#1", text="URL")
    for clave, valor in sites.items():
        tabla.insert('',0,text=clave,values=valor)
    window.mainloop()

def show_apps():
    window = Tk()
    window.resizable(0,0)
    window.title("Aplicaciones")
    window.configure(bg="black")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    frame1.config(bg="black", foreground="white")
    tabla = ttk.Treeview(frame1,columns=2)
    tabla.grid(row=0,column=0,padx=5,pady=5,columnspan=2)
    tabla.heading("#0", text="Clave o Nombre")
    tabla.heading("#1", text="Ruta")
    for clave, valor in apps.items():
        tabla.insert('',0,text=clave,values=valor)
    window.mainloop()


if __name__ == "__main__":
    talk("Hola, soy Cortana")
    window = Tk()
    window.resizable(0,0)
    window.title("Asistente Virtual UwU")
    window.configure(bg="black")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    frame1.config(bg="black", foreground="white")
    Label(frame1,text="Lista de comandos", bg="black", fg="white").grid(row=0,column=0,padx=10,pady=10,sticky=W+E)
    Label(frame1,text="'Reproduce ???: Reproducir una canción en YouTube", bg="black", fg="white").grid(row=1,column=0,padx=5,pady=5,sticky=W+E)
    Label(frame1,text="'Abre ???': Abrir un sitio Web o aplicacion del equipo", bg="black", fg="white").grid(row=2,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Busca ???': Realizar una busqueda en Google", bg="black", fg="white").grid(row=3,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Dime la hora': Decir la hora actual", bg="black", fg="white").grid(row=4,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Dime la fecha de hoy': Decir la fecha actual", bg="black", fg="white").grid(row=5,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Apagar': Terminar la interaccion", bg="black", fg="white").grid(row=6,column=0,padx=5,pady=5,sticky=W)
    frame2 = LabelFrame(window)
    frame2.grid(row=1,column=0,padx=10,pady=10)
    frame2.config(bg="black", foreground="white")
    Button(frame2,text="Iniciar", command=run_cortana, bg="black", fg="white").grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W+E)
    Button(frame2,text="Agregar Sitio Web", command=add_web_window, bg="black", fg="white", width=20).grid(row=1,column=0,padx=5,pady=5)
    Button(frame2,text="Agregar Aplicación", command=add_app_window, bg="black", fg="white", width=20).grid(row=1,column=1,padx=5,pady=5)
    Button(frame2,text="Consultar Sitios Web", command=show_web, bg="black", fg="white", width=20).grid(row=2,column=0,padx=5,pady=5)
    Button(frame2,text="Consultar Aplicaciones", command=show_apps, bg="black", fg="white", width=20).grid(row=2,column=1,padx=5,pady=5)
    window.mainloop()