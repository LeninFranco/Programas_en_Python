# Instalar los siguientes paquetes
# 1. pip install SpeechRecognition
# 2. pip install pyttsx3
# 3. pip install PyAudio
# 4. pip install pywhatkit

import speech_recognition as sr
import pyttsx3, pywhatkit
import subprocess as sub
import os

#Las direcciones Web deben existir (Comando "abre")
sites = {
    "monas chinas": "https://www3.animeflv.net/",
    "facebook": "https://www.facebook.com/",
    "youtube": "https://www.youtube.com/",
    "google": "https://www.google.com.mx/?hl=es-419",
    "whatsapp": "https://web.whatsapp.com/",
    "wikipedia": "https://es.wikipedia.org/wiki/Wikipedia:Portada",
    "udemy": "https://www.udemy.com/",
    "cuevana": "https://cuevana3.io/",
    "repositorios": "https://github.com/",
    "luchitas falsas": "https://latinlucha.es/"
}

#Las direcciones deben ser de tus archivos y programas que tengas instalados (Comando "inicia")
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
            pc = listener.listen(source, phrase_time_limit=4)
            rec = listener.recognize_google(pc, language="es-MX")
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
    if 'inicia' in rec:
        for app in apps:
            if app in rec:
                os.startfile(apps[app])
                talk(f'Iniciando {app}')
                return True
    if 'silencio' in rec:
        print("No te escuho")
        talk("¿En que puedo ayudarte?")
        return True
    if 'apagar' in rec:
        print("Apagando nos vemos")
        talk("Apagando nos vemos")
        return False
    print("No te entiendo")
    talk("No te entiendo, podrias repetir tu peticion de nuevo por favor")
    return True


if __name__ == "__main__":
    ban = True
    talk("Hola soy cortana, ¿En que puedo ayudarte?")
    while(ban):
        ban = run_cortana()