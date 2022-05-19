# Instalar los siguientes paquetes para el correcto funcionamiento
# 1. pip install SpeechRecognition
# 2. pip install pyttsx3
# 3. pip install PyAudio
# 4. pip install pywhatkit
# 5. pip install wikipedia

from tkinter import messagebox #Ventanas emergentes de la libreria tkinter
from tkinter import ttk #Extensiones de la libreria tkinter
from tkinter import * #Todos las clases de interfaz grafica de tkinter
import sqlite3 #Manejo de bases de datos SQLite
import speech_recognition as sr #Reconocimiento de voz
import pyttsx3, pywhatkit #Manejo del reconocimiento de voz y reproduccion de YouTube respectivamente
import os #Manejo del sistema operativo con llamadas al sistema
from datetime import datetime #Clase de tiempo
import wikipedia #Consultar informacion de Wikipedia
import re #Expresiones regulares
import webbrowser as wb #Abrir sitios en el navegador por defecto
import lib.SpeechMath as sm #Libreria propia para calculos matematicos por voz

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

#Se nombra al asistente virtual y se instancia el reconocedor de voz y su manejador
name = "iris"
listener = sr.Recognizer()
engine = pyttsx3.init()

#Se asigna una voz a la asistente virtual
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#Funcion que reproduce en voz un texto
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Funcion que reconoce la voz y la transcribe a texto en español
def listen():
    try:
        with sr.Microphone() as source:
            talk("Te escucho")
            pc = listener.listen(source, phrase_time_limit=5)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            return rec
    except:
        return "silencio"

#Función para reproducir música
def playMusic(rec):
    music = rec.replace('reproduce','')
    talk("Reproduciendo " + music)
    pywhatkit.playonyt(music)

#Función para abrir una aplicación o sitio Web
def openAppWeb(rec):
    band = False
    for site in sites:
        if site in rec:
            wb.open(sites[site])
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

#Función para realizar una búsqueda en Google en el navegador
def googleSearch(rec):
    search = rec.replace('busca','')
    search = search.split()
    wb.open('https://google.com/search?q='+'+'.join(search))
    talk("Encontre estos resultados")

#Función para obtener la fecha y la hora
def getDate(datetype):
    now = datetime.now()
    if datetype == "hora":
        talk(f"Son las {now.hour} horas con {now.minute} minutos")
    elif datetype == "fecha":
        talk(f"Hoy es {now.day} de {months[str(now.month)]} de {now.year}")
    else:
        talk("No se que hacer")

#Función para explicar una definición, personaje, explicación de wikipedia
def wikipediaSearch(rec, question):
    if question == "define":
        search = rec.replace('define','')
        getWikipediaInfo(search)
    elif question == "explica":
        search = rec.replace('explica','')
        getWikipediaInfo(search)
    elif question == "qué es":
        search = rec.replace('qué es','')
        getWikipediaInfo(search)
    elif question == "quién es":
        search = rec.replace('quién es','')
        getWikipediaInfo(search)
    else:
        talk("No se que hacer")

#Obtiene información en la API de Wikipedia
def getWikipediaInfo(search):
    try:
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(search,2)
        wiki = re.sub(r'\[[\w\s]+\]','',wiki)
        talk(wiki)
    except:
        talk("No te entiendo lo que solicitas")

#Funcion principal del asistente, ejecuta operaciones de acuerdo a un comando o palabra clave
def runIris():
    while(True):
        rec = listen() 
        print(rec) 
        if name in rec: 
            rec = rec.replace(name,'') 
            if 'reproduce' in rec: 
                playMusic(rec)
                continue
            if 'abre' in rec:
                openAppWeb(rec)
                continue
            if 'busca' in rec:
                googleSearch(rec)
                continue
            if 'dime la hora' in rec:
                getDate("hora")
                continue
            if 'dime la fecha de hoy' in rec:
                getDate("fecha")
                continue
            if 'qué eres' in rec or 'eres' in rec:
                talk("Soy " + name + ", un asistente virtual desarrollado en el lenguaje de programación Python")
                continue
            if 'define' in rec:
                wikipediaSearch(rec,"define")
                continue
            if 'explica' in rec:
                wikipediaSearch(rec,"explica")
                continue
            if 'qué es' in rec:
                wikipediaSearch(rec,"qué es")
                continue
            if 'quién es' in rec:
                wikipediaSearch(rec,"quién es")
                continue
            if 'cuánto' in rec:
                talk(sm.getResult(rec))
                continue
            talk("No te entiendo, podrias repetir tu peticion de nuevo por favor")
            continue
        if 'hola' in rec:
            talk("Hola, un gusto")
            continue
        if 'gracias' in rec:
            talk("A sus ordenes")
            continue
        if 'apagar' in rec or 'adiós' in rec:
            talk("Apagando, nos vemos")
            break
        if 'silencio' in rec:
            continue

#Ventana para añadir sitios Web a la base de datos
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

#Funcion que añade a la base de datos el sitio Web introducido por el usuario
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

#Ventana para añadir aplicaciones a la base de datos
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

#Funcion que añade a la base de datos la aplicacion introducido por el usuario
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

#Ventana para eliminar un sitio Web
def drop_web_window():
    global eClaveWeb, window
    window = Tk()
    window.resizable(0,0)
    window.title("Eliminar Sitio Web")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    Label(frame1,text="Nombre o Palabra Clave").grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
    sql = sqlite3.connect("AS.db")
    cursor = sql.execute('''SELECT * FROM sitios''')
    filas = cursor.fetchall()
    lista = [fila[0] for fila in filas]
    sql.close()
    eClaveWeb = ttk.Combobox(frame1,width=50,state='readonly',values=lista)
    eClaveWeb.grid(row=1,column=0,padx=5,pady=5)
    Button(frame1,text="Eliminar",command=drop_web).grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
    window.mainloop()

#Funcion que elimina de la base de datos un sitio web
def drop_web():
    if eClaveWeb.get() != "":
        clave = eClaveWeb.get()
        sql = sqlite3.connect("AS.db")
        sql.execute('''DELETE FROM sitios WHERE clave=?''',(clave,))
        sql.commit()
        del(sites[clave])
        messagebox.showinfo(message="Sitio Web eliminada correctamente", title="EXITO")
        eClaveWeb.delete(0,END)
        sql.close()
        window.destroy()
    else:
        messagebox.showwarning(message="Favor de escoger el sitio Web", title="ADVERTENCIA")

#Ventana para eliminar una App
def drop_app_window():
    global eClaveApp, window
    window = Tk()
    window.resizable(0,0)
    window.title("Eliminar Aplicación")
    frame1 = LabelFrame(window)
    frame1.grid(row=0,column=0,padx=10,pady=10)
    Label(frame1,text="Nombre o Palabra Clave").grid(row=0,column=0,padx=5,pady=5,sticky=W+E)
    sql = sqlite3.connect("AS.db")
    cursor = sql.execute('''SELECT * FROM apps''')
    filas = cursor.fetchall()
    lista = [fila[0] for fila in filas]
    sql.close()
    eClaveApp = ttk.Combobox(frame1,width=50,state='readonly',values=lista)
    eClaveApp.grid(row=1,column=0,padx=5,pady=5)
    Button(frame1,text="Eliminar",command=drop_app).grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
    window.mainloop()

#Funcion que elimina de la base de datos una app
def drop_app():
    if eClaveApp.get() != "":
        clave = eClaveApp.get()
        sql = sqlite3.connect("AS.db")
        sql.execute('''DELETE FROM apps WHERE clave=?''',(clave,))
        sql.commit()
        del(apps[clave])
        messagebox.showinfo(message="Aplicación eliminada correctamente", title="EXITO")
        sql.close()
        window.destroy()
    else:
        messagebox.showwarning(message="Favor de escoger la aplicación", title="ADVERTENCIA")

#Ventana que muestra una tabla con los sitios Web de la base de datos
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
    scrollbar = ttk.Scrollbar(window)
    scrollbar.configure(command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0,column=1,padx=10,pady=10, sticky=S+E+N)
    for clave, valor in sites.items():
        tabla.insert('',0,text=clave,values=valor)
    window.mainloop()

#Ventana que muestra una tabla con las aplicaciones de la base de datos
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
    scrollbar = ttk.Scrollbar(window)
    scrollbar.configure(command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0,column=1,padx=10,pady=10, sticky=S+E+N)
    for clave, valor in apps.items():
        tabla.insert('',0,text=clave,values=valor)
    window.mainloop()

#Funcion Main
if __name__ == "__main__":
    talk("Hola, soy " + name)
    window = Tk()
    window.resizable(0,0)
    window.title("Asistente Virtual UwU")
    frame2 = LabelFrame(window)
    frame2.grid(row=1,column=0,padx=10,pady=10)
    Button(frame2,text="Iniciar", command=runIris).grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=W+E)
    Button(frame2,text="Agregar Sitio Web", command=add_web_window, width=20).grid(row=1,column=0,padx=5,pady=5)
    Button(frame2,text="Agregar Aplicación", command=add_app_window, width=20).grid(row=1,column=1,padx=5,pady=5)
    Button(frame2,text="Eliminar Sitio Web", command=drop_web_window, width=20).grid(row=2,column=0,padx=5,pady=5)
    Button(frame2,text="Eliminar Aplicación", command=drop_app_window, width=20).grid(row=2,column=1,padx=5,pady=5)
    Button(frame2,text="Consultar Sitios Web", command=show_web, width=20).grid(row=3,column=0,padx=5,pady=5)
    Button(frame2,text="Consultar Aplicaciones", command=show_apps, width=20).grid(row=3,column=1,padx=5,pady=5)
    window.mainloop()
