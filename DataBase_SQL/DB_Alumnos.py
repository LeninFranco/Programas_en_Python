import os
import sqlite3
#LA BOLETA ESTA FORMADA POR XXXXYYZZ
#X ES EL AÑO DE INGRESO A LA INSTITUCION
#Y CODIGO DE LA INSTITUCION
#Z EL ID

#EL GRUPO ESTA FORMADO POR EL SIGUIENTE FORMATO ABCXX
#A ES EL NUMERO DE SEMESTRE {1,2:TRONCO COMUN, 3-6:CARRERA TECNICA}
#B ES LA CARRERA TECNICA {I:INFORMATICA,C:CONTABILIDAD,D:DERECHO,T:TRONCO COMUN}
#C ES LA INICIAL DEL TURNO {M:MATUTINO,V:VESPERTINO}
#X ES EL NUMERO DEL GRUPO {RANGO: 1-12}

#Clase Alumno
class Alumno:
    def __init__(self,Boleta,Nombre,Apellido,Carrera,Turno,Grupo,Promedio):
        self.Boleta = Boleta
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Carrera = Carrera
        self.Turno = Turno
        self.Grupo = Grupo
        self.Promedio = Promedio

#Funciones de la Base de Datos
def Insert(sql,A):
    cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE BOLETA=?''',(A.Boleta,))
    fila = cursor.fetchone()
    if fila == None:
        sql.execute('''INSERT INTO ALUMNOS(BOLETA,NOMBRE,APELLIDO,CARRERA,TURNO,GRUPO,PROMEDIO) VALUES(?,?,?,?,?,?,?)''',(A.Boleta,A.Nombre,A.Apellido,A.Carrera,A.Turno,A.Grupo,A.Promedio))
        print("Se ha guardado el alumno correctamente")
    else:
        print("Ya existe un alumno con la misma boleta ingresada")
    sql.commit()

def Delete(sql,A):
    cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE BOLETA=?''',(A.Boleta,))
    fila = cursor.fetchone()
    if fila != None:
        sql.execute('''DELETE FROM ALUMNOS WHERE BOLETA=?''',(A.Boleta,))
        print("Se ha eliminado el alumno correctamente")
    else:
        print("No se ha encontrado al alumno a eliminar")
    sql.commit()

def Search(sql,A):
    cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE BOLETA=?''',(A.Boleta,))
    fila = cursor.fetchall()
    if fila != None:
        print("Se ha encontrado el alumno correctamente")
        for i in fila:
            print("----------------------------------------------------")
            print(f"Boleta: {i[0]}")
            print(f"Nombre: {i[1]}")
            print(f"Apellido: {i[2]}")
            print(f"Carrera: {i[3]}")
            print(f"Turno: {i[4]}")
            print(f"Grupo: {i[5]}")
            print(f"Promedio: {i[6]}")
            print("----------------------------------------------------")
    else:
        print("No se ha encontrado al alumno")

def Edit(sql,A,opc2):
    new_data = ""
    cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE BOLETA=?''',(A.Boleta,))
    fila = cursor.fetchone()
    if fila != None:
        if opc2 == 1:
            new_data = input("Ingrese la nueva Boleta: ")
            sql.execute('''UPDATE ALUMNOS SET BOLETA=? WHERE BOLETA=?''',(new_data,A.Boleta))
        elif opc2 == 2:
            new_data = input("Ingrese el nuevo Nombre: ")
            sql.execute('''UPDATE ALUMNOS SET NOMBRE=? WHERE BOLETA=?''',(new_data,A.Boleta))
        elif opc2 == 3:
            new_data = input("Ingrese el nuevo Apellido: ")
            sql.execute('''UPDATE ALUMNOS SET APELLIDO=? WHERE BOLETA=?''',(new_data,A.Boleta))
        elif opc2 == 4:
            new_data = input("Ingrese la nueva Carrera: ")
            new_data = new_data.upper()
            sql.execute('''UPDATE ALUMNOS SET CARRERA=? WHERE BOLETA=?''',(new_data,A.Boleta))
        elif opc2 == 5:
            new_data = input("Ingrese el nuevo Turno: ")
            new_data = new_data.upper()
            sql.execute('''UPDATE ALUMNOS SET TURNO=? WHERE BOLETA=?''',(new_data,A.Boleta))
        elif opc2 == 6:
            new_data = input("Ingrese el nuevo Grupo: ")
            new_data = new_data.upper()
            sql.execute('''UPDATE ALUMNOS SET NOMBRE=? WHERE BOLETA=?''',(new_data,A.Boleta))
        elif opc2 == 7:
            new_data = float(input("Ingrese el nuevo Promedio: "))
            sql.execute('''UPDATE ALUMNOS SET PROMEDIO=? WHERE BOLETA=?''',(new_data,A.Boleta))
        print("Los datos han sido actualizados")
    else:
        print("No se ha encontrado al alumno para editar")
    sql.commit()

def Show(sql,opc2):
    if opc2 == 1:
        data = input("Ingrese la Carrera: ")
        data = data.upper()
        cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE CARRERA=? ORDER BY APELLIDO ASC''',(data,))
        filas = cursor.fetchall()
        print("Se ha encontrado la informacion requerida")
        for i in filas:
            print("----------------------------------------------------")
            print(f"Boleta: {i[0]}")
            print(f"Nombre: {i[1]}")
            print(f"Apellido: {i[2]}")
            print(f"Carrera: {i[3]}")
            print(f"Turno: {i[4]}")
            print(f"Grupo: {i[5]}")
            print(f"Promedio: {i[6]}")
            print("----------------------------------------------------")
    elif opc2 == 2:
        data = input("Ingrese el Turno: ")
        data = data.upper()
        cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE TURNO=? ORDER BY APELLIDO ASC''',(data,))
        filas = cursor.fetchall()
        print("Se ha encontrado la informacion requerida")
        for i in filas:
            print("----------------------------------------------------")
            print(f"Boleta: {i[0]}")
            print(f"Nombre: {i[1]}")
            print(f"Apellido: {i[2]}")
            print(f"Carrera: {i[3]}")
            print(f"Turno: {i[4]}")
            print(f"Grupo: {i[5]}")
            print(f"Promedio: {i[6]}")
            print("----------------------------------------------------")
    elif opc2 == 3:
        data = input("Ingrese el Grupo: ")
        data = data.upper()
        cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE GRUPO=? ORDER BY APELLIDO ASC''',(data,))
        filas = cursor.fetchall()
        print("Se ha encontrado la informacion requerida")
        for i in filas:
            print("----------------------------------------------------")
            print(f"Boleta: {i[0]}")
            print(f"Nombre: {i[1]}")
            print(f"Apellido: {i[2]}")
            print(f"Carrera: {i[3]}")
            print(f"Turno: {i[4]}")
            print(f"Grupo: {i[5]}")
            print(f"Promedio: {i[6]}")
            print("----------------------------------------------------")
    elif opc2 == 4:
        cursor = sql.execute('''SELECT * FROM ALUMNOS WHERE PROMEDIO>=8 ORDER BY APELLIDO ASC''')
        filas = cursor.fetchall()
        print("Se ha encontrado la informacion requerida")
        for i in filas:
            print("----------------------------------------------------")
            print(f"Boleta: {i[0]}")
            print(f"Nombre: {i[1]}")
            print(f"Apellido: {i[2]}")
            print(f"Carrera: {i[3]}")
            print(f"Turno: {i[4]}")
            print(f"Grupo: {i[5]}")
            print(f"Promedio: {i[6]}")
            print("----------------------------------------------------")
    sql.commit()

#Funciones del Programa
def Menu_Principal():
    while True:
        os.system("cls")
        print("**********MENU PRINCIPAL**********")
        print("1. GUARDAR NUEVO ALUMNO")
        print("2. ELIMINAR ALUMNO")
        print("3. BUSCAR ALUMNO")
        print("4. EDITAR DATOS DEL ALUMNO")
        print("5. MOSTRAR ALUMNOS")
        print("6. SALIR")
        opc = input(">>> ")
        try:
            int(opc)
        except:
            continue
        opc = int(opc)
        if(opc<1 or opc>6):
            continue
        else:
            return opc
            break
def Menu_Edicion():
    while True:
        os.system("cls")
        print("**********MENU DE EDICION**********")
        print("1. EDITAR BOLETA")
        print("2. EDITAR NOMBRE")
        print("3. EDITAR APELLIDO")
        print("4. EDITAR CARRERA")
        print("5. EDITAR TURNO")
        print("6. EDITAR GRUPO")
        print("7. EDITAR PROMEDIO")
        print("8. REGRESAR AL MENU PRINCIPAL")
        opc = input(">>> ")
        try:
            int(opc)
        except:
            continue
        opc = int(opc)
        if(opc<1 or opc>9):
            continue
        else:
            return opc
            break
def Menu_Filtro():
    while True:
        os.system("cls")
        print("**********MENU DE SALIDA**********")
        print("LOS ALUMNOS SE ORDENARAN DE MANERA ASCENDENTE POR APELLIDO")
        print("1. MOSTRAR ALUMNOS DE UNA CARRERA ESPECIFICA")
        print("2. MOSTRAR ALUMNOS DE UN TURNO ESPECIFICO")
        print("3. MOSTRAR ALUMNOS DE UN GRUPO ESPECIFICO")
        print("4. MOSTRAR ALUMNOS CUYO PROMEDIO ES DE EXCELENCIA(MAYOR E IGUAL A 8)")
        print("5. REGRESAR AL MENU PRINCIPAL")
        opc = input(">>> ")
        try:
            int(opc)
        except:
            continue
        opc = int(opc)
        if(opc<1 or opc>6):
            continue
        else:
            return opc
            break
#Main
os.system("cls")
sql = sqlite3.connect("DataBase_Alumnos.db")
while True:
    opc1 = Menu_Principal()
    if opc1 == 1:
        boleta = input("Ingrese la Boleta: ")
        nombre = input("Ingrese el Nombre: ")
        apellido = input("Ingrese el Apellido: ")
        carrera = input("Ingrese la carrera: ")
        turno = input("Ingrese el Turno: ")
        grupo = input("Ingrese el Grupo: ")
        promedio = float(input("Ingrese el Promedio: "))
        A = Alumno(boleta,nombre,apellido,carrera,turno,grupo,promedio)
        Insert(sql,A)
    elif opc1 == 2:
        boleta = input("Ingrese la Boleta: ")
        A = Alumno(boleta,"","","","","",0)
        Delete(sql,A)
    elif opc1 == 3:
        boleta = input("Ingrese la Boleta: ")
        A = Alumno(boleta,"","","","","",0)
        Search(sql,A)
    elif opc1 == 4:
        while True:
            opc2 = Menu_Edicion()
            if opc2 == 1:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 2:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 3:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 4:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 5:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 6:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 7:
                boleta = input("Ingrese la Boleta: ")
                A = Alumno(boleta,"","","","","",0)
                Edit(sql,A,opc2)
            elif opc2 == 8:
                break
            else:
                continue
            os.system("Pause")
    elif opc1 == 5:
        while True:
            opc2 = Menu_Filtro()
            if opc2 == 1:
                Show(sql,opc2)
            elif opc2 == 2:
                Show(sql,opc2)
            elif opc2 == 3:
                Show(sql,opc2)
            elif opc2 == 4:
                Show(sql,opc2)
            elif opc2 == 5:
                break
            else:
                continue
            os.system("Pause")
    elif opc1 == 6:
        print("Gracias por usarme UwU")
        break
    else:
        continue
    os.system("Pause")
sql.close()
os.system("Pause")