from os import system
import re


palabras = {}

def normalizar(palabra):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    aux = re.sub("[.,\/#\¡!\¿?$%\^&\*;:{}=\-_`~()\"…]","",palabra.lower())
    for a,b in replacements:
        aux = aux.replace(a,b)
    return aux


def repeticionesPalabras(text):
    separadas = text.split(' ')
    for palabra in separadas:
        if(normalizar(palabra) in palabras):
            palabras[normalizar(palabra)] += 1
        else:
            palabras[normalizar(palabra)] = 1

if __name__ == "__main__":
    texto = "Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma."
    repeticionesPalabras(texto)
    for key,value in palabras.items():
        print(f"{key} -> {value}")