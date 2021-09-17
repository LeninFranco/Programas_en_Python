import os   

draw = [
    '''
    *---*
    |   |
        |
        |
        |
        |
        ===========
    ''',
    '''
    *---*
    |   |
    O   |
        |
        |
        |
        ===========
    ''',
    '''
    *---*
    |   |
    O   |
    |   |
        |
        |
        ===========
    ''',
    '''
    *---*
    |   |
    O   |
    |\  |
        |
        |
        ===========
    ''',
    '''
    *---*
    |   |
    O   |
   /|\  |
        |
        |
        ===========
    ''',
   '''
    *---*
    |   |
    O   |
   /|\  |
     \  |
        |
        ===========
    ''',
    '''
    *---*
    |   |
    O   |
   /|\  |
   / \  |
        | DEATH
        ===========
    '''
]

os.system("cls")
Palabra = input("Ingrese la Palabra para el juego: ")
Palabra = Palabra.upper()
Lpalabra1 = []
Lpalabra2 = []
for i in Palabra:
    if i == " ":
        Lpalabra1.append(" ")
        Lpalabra2.append(" ")
    else:
        Lpalabra1.append(i)
        Lpalabra2.append("___")
vidas = 6
contdraw = 0
while True:
    os.system("cls")
    cont = 0
    band = False
    print()
    os.system("cls")
    print(draw[contdraw])
    print()
    print(" ".join(Lpalabra2))
    print()
    letra = input("Ingrese una letra >>> ")
    letra = letra.upper()
    for i in Lpalabra1:
        if letra == i:
            Lpalabra2[cont] = i
            band = True
        cont += 1
    if(band==False):
        vidas -= 1
        contdraw += 1
        print(f"Fallaste te quedan {vidas} vidas")
    if(band==True):
        print(f"Acertaste te quedan {vidas} vidas")
    if(vidas == 0):
        os.system("cls")
        print(draw[contdraw])
        print()
        print(" ".join(Lpalabra2))
        print("Fallaste carnal, suerte para la proxima")
        print(f"Respuesta: {Palabra}")
        break
    if(Lpalabra1 == Lpalabra2):
        os.system("cls")
        print(draw[contdraw])
        print()
        print(" ".join(Lpalabra2))
        print(f"Ganaste y te sobraron {vidas} vidas")
        break
    os.system("Pause")
os.system("Pause")

