import os

def HanoiTowerSolution(disc,t1,t2,t3):
    if disc == 1:
        print(f"Mover disco de la torre {t1} hacia la torre {t3}")
    else:
        HanoiTowerSolution(disc-1,t1,t3,t2)
        print(f"Mover disco de la torre {t1} hacia la torre {t3}")
        HanoiTowerSolution(disc-1,t2,t1,t3)

if __name__ == "__main__":
    os.system("cls")
    t1 = 1
    t2 = 2
    t3 = 3
    disc = int(input("Ingrese el numero de discos: "))
    HanoiTowerSolution(disc,t1,t2,t3)
