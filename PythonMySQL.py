import os
import pymysql

class DataBase: 
    #Creamos la conexion a la base de datos y creamos el cursor
    def __init__(self):
        self.conexion = pymysql.Connect(
            host='localhost',
            user='root',
            password='P0L1m4s7er!',
            db='jdbc'
        )
        self.cursor = self.conexion.cursor()
        print("Conexion Exitosa")
    #Metodo para cerrar la conexion
    def close(self):
        self.cursor.close()
        self.conexion.close()
        print("Conexion cerrada")
    #Metodo para consultar una sola fila
    def sel_one(self, id):
        sql = "SELECT * FROM canciones WHERE idCancion=%s"
        try:
            self.cursor.execute(sql,(id))
            fila = self.cursor.fetchone()
            print("{:<5} {:<30} {:<30} {:<20} {:<7} {:<10}".format("ID","Nombre","Album","Artista","Año","Duracion"))
            print("-"*105)
            print("{:<5} {:<30} {:<30} {:<20} {:<7} {:<10}".format(fila[0],fila[1],fila[2],fila[3],fila[4],str(fila[5])))
            print("-"*105)
        except Exception as e:
            print("No se encontro la cancion")
    #Metodo para consultar multiples filas
    def sel_all(self):
        sql = "SELECT * FROM canciones"
        try:
            self.cursor.execute(sql)
            filas = self.cursor.fetchall()
            print("{:<5} {:<30} {:<30} {:<20} {:<7} {:<10}".format("ID","Nombre","Album","Artista","Año","Duracion"))
            print("-"*105)
            for i in filas:
                print("{:<5} {:<30} {:<30} {:<20} {:<7} {:<10}".format(i[0],i[1],i[2],i[3],i[4],str(i[5])))
                print("-"*105)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    db = DataBase()
    db.sel_all()
    db.close()