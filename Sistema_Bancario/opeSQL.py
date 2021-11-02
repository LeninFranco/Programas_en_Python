import sqlite3

class Usuario:
    def __init__(self,cuenta,nombre,apellido,password,saldo):
        self.cuenta = cuenta
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.saldo = saldo

class Operaciones:
    @staticmethod
    def findall():
        conn = sqlite3.connect("banco.db")
        cursor = conn.execute('''SELECT * FROM users''')
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios
    @staticmethod
    def findone(cuenta):
        conn = sqlite3.connect("banco.db")
        cursor = conn.execute('''SELECT * FROM users WHERE cuenta=?''',(cuenta,))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario
    @staticmethod
    def create(usuario):
        conn = sqlite3.connect("banco.db")
        cursor = conn.execute('''INSERT INTO users(cuenta,nombre,apellido,password,saldo) VALUES(?,?,?,?,?)''',(usuario.cuenta,usuario.nombre,usuario.apellido,usuario.password,usuario.saldo))
        conn.commit()
        cursor.close()
        conn.close()
    @staticmethod
    def delete(cuenta):
        conn = sqlite3.connect("banco.db")
        cursor = conn.execute('''DELETE FROM users WHERE cuenta=?''',(cuenta,))
        conn.commit()
        cursor.close()
        conn.close()
    @staticmethod
    def update(usuario):
        conn = sqlite3.connect("banco.db")
        cursor = conn.execute('''UPDATE users SET nombre=?,apellido=?,password=?,saldo=? WHERE cuenta=?''',(usuario.nombre,usuario.apellido,usuario.password,usuario.saldo,usuario.cuenta))
        conn.commit()
        cursor.close()
        conn.close()