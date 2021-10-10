import random
from os import system

elementos = {1:"Piedra",2:"Papel",3:"Tijera"}

def Jugar():
    while True:
        system("cls")
        jugador = int(input("Escoge una opcion (1 es Piedra, 2 es Papel, 3 es Tijera y 0 para salir): "))
        computadora = random.choice([1,2,3])

        if jugador == 0:
            break

        system("cls")
    
        print(f"[Jugador]: {elementos[jugador]}\n")
        print(f"[Skynet]: {elementos[computadora]}\n")
    
        if jugador == computadora:
            print("¡Empate!\n")
        elif victoria_jugador(jugador,computadora):
            print("¡Le ganaste a Skynet!\n")
        else:
            print("¡Skynet te ha ganado!\n")

        system("Pause")

def victoria_jugador(jugador,computadora):
    if((jugador == 1 and computadora == 3) or (jugador == 3 and computadora == 2) or (jugador == 2 and computadora == 1)):
        return True
    return False

if __name__ == "__main__":
    Jugar()
