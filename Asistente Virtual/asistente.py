# Instalar los siguientes paquetes para el correcto funcionamiento
# 1. pip install SpeechRecognition
# 2. pip install pyttsx3
# 3. pip install PyAudio
# 4. pip install pywhatkit

import speech_recognition as sr
import pyttsx3, pywhatkit
import subprocess as sub
import os
from datetime import datetime

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
    "spotify": r"C:\Users\Lenin Franco\AppData\Roaming\Spotify\Spotify.exe",
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
            if name in rec:
                rec = rec.replace(name,'')
            return rec
    except:
        return "silencio"

def run_cortana():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        talk("Reproduciendo " + music)
        pywhatkit.playonyt(music)
        return True
    if 'abre' in rec:
        for site in sites:
            if site in rec:
                sub.call(f'start chrome.exe {sites[site]}', shell=True)
                talk(f'Abriendo {site}')
                return True
        for app in apps:
            if app in rec:
                os.startfile(apps[app])
                talk(f'Abriendo {app}')
                return True
    if 'busca' in rec:
        search = rec.replace('busca','')
        search = search.split()
        sub.call('start chrome.exe https://google.com/search?q='+'+'.join(search), shell=True)
        talk("Encontre estos resultados")
        return True
    if 'dime la hora' in rec:
        now = datetime.now()
        talk(f"Son las {now.hour} horas con {now.minute} minutos")
        return True
    if 'dime la fecha de hoy' in rec:
        now = datetime.now()
        talk(f"Hoy es {now.day} de {months[str(now.month)]} de {now.year}")
        return True
    if 'silencio' in rec:
        print("No te escuho")
        talk("¿En que puedo ayudarte?")
        return True
    if 'apagar' in rec:
        print("Apagando, nos vemos")
        talk("Apagando, nos vemos")
        return False
    print("No te entiendo")
    talk("No te entiendo, podrias repetir tu peticion de nuevo por favor")
    return True

if __name__ == "__main__":
    ban = True
    talk("Hola soy cortana, ¿En que puedo ayudarte?")
    while(ban):
        ban = run_cortana()
