# Instalar los siguientes paquetes para el correcto funcionamiento
# 1. pip install SpeechRecognition
# 2. pip install pyttsx3
# 3. pip install PyAudio
# 4. pip install pywhatkit

from tkinter import messagebox
from tkinter import ttk
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
sites = {
    "monas chinas": "https://www3.animeflv.net/",
    "facebook": "https://www.facebook.com/",
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com.mx/?hl=es-419",
    "whatsapp": "https://web.whatsapp.com/",
    "udemy": "https://www.udemy.com/",
    "cuevana": "https://cuevana3.io/",
    "repositorios": "https://github.com/",
    "luchitas falsas": "https://latinlucha.es/"
}

#Las direcciones deben ser de tus archivos y programas que tengas instalados (Comando "abre")
apps = {
    "spotify": "C:\\Users\\Lenin Franco\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "word": "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "excel": "C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "power": "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "visual": "C:\\Users\Lenin Franco\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "consola": "C:\\WINDOWS\\system32\\cmd.exe",
    "notas": "C:\\WINDOWS\\system32\\notepad.exe"
}

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
        if 'silencio' in rec:
            talk("No te escucho, ¿en que puedo ayudarte?")
            continue
        if 'apagar' in rec:
            talk("Apagando, nos vemos")
            break
        talk("No te entiendo, podrias repetir tu peticion de nuevo por favor")

def add_web_window():
    global eClaveWeb, eValorWeb
    window = Tk()
    window.resizable(0,0)
    window.title("Agregar un Sitio Web")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    Label(frame1,text="Nombre o Palabra Clave").grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
    eClaveWeb = Entry(frame1,width=50)
    eClaveWeb.grid(row=1,column=0,padx=5,pady=5)
    Label(frame1,text="URL del Sitio Web").grid(row=2,column=0,padx=5,pady=5,sticky=W+E)
    eValorWeb = Entry(frame1,width=50)
    eValorWeb.grid(row=3,column=0,padx=5,pady=5)
    Button(frame1,text="Agregar",command=add_web).grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
    window.mainloop()

def add_web():
    if eClaveWeb.get().strip() != "" or eValorWeb.get().strip() != "":
        sites[eClaveWeb.get().strip()] = eValorWeb.get().strip()
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
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    Label(frame1,text="Nombre o Palabra Clave").grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
    eClaveApp = Entry(frame1,width=50)
    eClaveApp.grid(row=1,column=0,padx=5,pady=5)
    Label(frame1,text="Ruta de la Aplicación").grid(row=2,column=0,padx=5,pady=5,sticky=W+E)
    eValorApp = Entry(frame1,width=50)
    eValorApp.grid(row=3,column=0,padx=5,pady=5)
    Button(frame1,text="Agregar",command=add_app).grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
    window.mainloop()

def add_app():
    if eClaveApp.get().strip() != "" or eValorApp.get().strip() != "":
        direccion = eValorApp.get().strip()
        direccion = direccion.rsplit("\n")
        apps[eClaveApp.get().strip()] = direccion[0]
        messagebox.showinfo(message="Aplicacion agregada correctamente", title="OPERACION EXITOSA")
        eClaveApp.delete(0,"end")
        eValorApp.delete(0,"end")
    else:
        messagebox.showwarning(message="Favor de llenar todos los campos", title="ADVERTENCIA")

def show_web():
    window = Tk()
    window.resizable(0,0)
    window.title("Sitios Web")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
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
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    tabla = ttk.Treeview(frame1,columns=2)
    tabla.grid(row=0,column=0,padx=5,pady=5,columnspan=2)
    tabla.heading("#0", text="Clave o Nombre")
    tabla.heading("#1", text="Ruta")
    for clave, valor in apps.items():
        tabla.insert('',0,text=clave,values=valor)
    window.mainloop()


if __name__ == "__main__":
    window = Tk()
    window.resizable(0,0)
    window.title("Asistente Virtual UwU")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    Label(frame1,text="Lista de comandos").grid(row=0,column=0,padx=10,pady=10,sticky=W+E)
    Label(frame1,text="'Reproduce ???: Reproducir una canción en YouTube").grid(row=1,column=0,padx=5,pady=5,sticky=W+E)
    Label(frame1,text="'Abre ???': Abrir un sitio Web o aplicacion del equipo").grid(row=2,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Busca ???': Realizar una busqueda en Google").grid(row=3,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Dime la hora': Decir la hora actual").grid(row=4,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Dime la fecha de hoy': Decir la fecha actual").grid(row=5,column=0,padx=5,pady=5,sticky=W)
    Label(frame1,text="'Apagar': Terminar la interaccion").grid(row=6,column=0,padx=5,pady=5,sticky=W)
    frame2 = LabelFrame(window)
    frame2.grid(row=1,column=0,padx=10,pady=10)
    Button(frame2,text="Iniciar", command=run_cortana).grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W+E)
    Button(frame2,text="Agregar Sitio Web", command=add_web_window).grid(row=1,column=0,padx=5,pady=5)
    Button(frame2,text="Agregar Aplicación", command=add_app_window).grid(row=1,column=1,padx=5,pady=5)
    Button(frame2,text="Consultar Sitios Web", command=show_web).grid(row=2,column=0,padx=5,pady=5)
    Button(frame2,text="Consultar Aplicaciones", command=show_apps).grid(row=2,column=1,padx=5,pady=5)
    talk("Hola soy Cortana")
    window.mainloop()
