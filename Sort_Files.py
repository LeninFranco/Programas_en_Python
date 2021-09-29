import os 
import shutil

ruta_archivos = "C:\\Users\\Lenin Franco\\Downloads\\Programas Python\\Sort_Files_Python\\"
ext_docs = ['.docx','.txt','.doc','.pdf']
ext_imag = ['.png','.jpg','.jpeg','.gif']
ext_video = ['.mp4']
ext_music = ['.mp3']

def Ordenar(archivo, ext):
    for i in ext_docs:
        if ext == i:
            shutil.move(ruta_archivos+archivo,ruta_archivos+"Documentos")
    for i in ext_imag:
        if ext == i:
            shutil.move(ruta_archivos+archivo,ruta_archivos+"Imagenes")
    for i in ext_video:
        if ext == i:
            shutil.move(ruta_archivos+archivo,ruta_archivos+"Videos")
    for i in ext_music:
        if ext == i:
            shutil.move(ruta_archivos+archivo,ruta_archivos+"Musica")

def main():
    for archivo in os.listdir(ruta_archivos):
        nombre_archivo, ext = os.path.splitext(archivo)
        Ordenar(archivo,ext)

main()
print("LA OPERACION SE HA REALIZADO CON EXITO")
os.system("Pause")