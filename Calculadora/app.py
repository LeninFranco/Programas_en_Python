from os import system
from basic_math import *
from menu import *

while True:
    system("cls")
    opc = MainMenu()
    if opc == 1:
        nums = SubMenu()
        if nums == -1:
            continue
        else:
            print(f"El resultado de la suma es: {suma(nums[0],nums[1])}")
    elif opc == 2: 
        nums = SubMenu()
        if nums == -1:
            continue
        else:
            print(f"El resultado de la resta es: {resta(nums[0],nums[1])}")
    elif opc == 3:
        nums = SubMenu()
        if nums == -1:
            continue
        else:
            print(f"El resultado de la multiplicacion es: {multiplicacion(nums[0],nums[1])}")
    elif opc == 4:
        nums = SubMenu()
        if nums == -1:
            continue
        else:
            print(f"El resultado de la division es: {division(nums[0],nums[1])}")
    elif opc == 5:
        print("Gracias por usarme")
        break
    else:
        continue
    system("pause")