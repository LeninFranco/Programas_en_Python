# Instalar los siguientes paquetes para el correcto funcionamiento
# 1. pip install SpeechRecognition
# 2. pip install pyttsx3
# 3. pip install PyAudio
# 4. pip install pywhatkit
# 5. pip install wikipedia

import speech_recognition as sr #Reconocimiento de voz
import pyttsx3, pywhatkit #Manejo del reconocimiento de voz y reproduccion de YouTube respectivamente
import os #Manejo del sistema operativo con llamadas al sistema
from datetime import datetime #Clase de tiempo
import wikipedia #Consultar informacion de Wikipedia
import re #Expresiones regulares
import webbrowser as wb #Abrir sitios en el navegador por defecto

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
    "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "power": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    "visual": r"C:\Users\Lenin Franco\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "consola": r"C:\WINDOWS\system32\cmd.exe",
    "notas": r"C:\WINDOWS\system32\notepad.exe"
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
            print("Escuchando...")
            pc = listener.listen(source, phrase_time_limit=5)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            return rec
    except:
        return "silencio"

def run_cortana():
    while(True):
        rec = listen() 
        print(rec) 
        if name in rec: 
            rec = rec.replace(name,'') 
            if 'reproduce' in rec: 
                music = rec.replace('reproduce','')
                talk("Reproduciendo " + music)
                pywhatkit.playonyt(music)
                continue
            if 'abre' in rec:
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
                continue
            if 'busca' in rec:
                search = rec.replace('busca','')
                search = search.split()
                wb.open('https://google.com/search?q='+'+'.join(search))
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
                talk("Soy " + name + ", un asistente virtual desarrollado en el lenguaje de programación Python")
                continue
            if 'define' in rec:
                try:
                    search = rec.replace('define','')
                    wikipedia.set_lang("es")
                    wiki = wikipedia.summary(search,1)
                    wiki = re.sub(r'\[[\w\s]+\]','',wiki)
                    talk(wiki)
                except:
                    talk("No te entiendo lo que solicitas")
                continue
            if 'explica' in rec:
                try:
                    search = rec.replace('explica','')
                    wikipedia.set_lang("es")
                    wiki = wikipedia.summary(search,1)
                    wiki = re.sub(r'\[[\w\s]+\]','',wiki)
                    talk(wiki)
                except:
                    talk("No te entiendo lo que solicitas")
                continue
            talk("No te entiendo, podrias repetir tu peticion de nuevo por favor")
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

if __name__ == "__main__":
    talk("Hola soy cortana, ¿En que puedo ayudarte?")
    run_cortana()
