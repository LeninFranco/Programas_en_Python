from Modelo import Producto
import sqlite3

class ProductoDAO:
    def getConnection(self):
        return sqlite3.connect("db\Productos.db")
    def create(self, producto: Producto):
        conn = self.getConnection()
        conn.execute('''INSERT INTO producto VALUES(?,?,?)''',(producto.ID,producto.nombre,producto.precio))
        conn.commit()
        conn.close()
    def update(self, producto: Producto):
        conn = self.getConnection()
        conn.execute('''UPDATE producto SET nombre=?, precio=? WHERE id=?''',(producto.nombre,producto.precio,producto.ID))
        conn.commit()
        conn.close()
    def delete(self,producto: Producto):
        conn = self.getConnection()
        conn.execute('''DELETE FROM producto WHERE id=?''',(producto.ID,))
        conn.commit()
        conn.close()
    def selectOne(self,producto: Producto):
        conn = self.getConnection()
        cursor = conn.execute('''SELECT * FROM producto WHERE id=?''',(producto.ID,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Producto(row[0], row[1], float(row[2]))
    def selectAll(self):
        conn = self.getConnection()
        cursor = conn.execute('''SELECT * FROM producto''')
        rows = cursor.fetchall()
        p = []
        for row in rows:
            p.append(Producto(row[0], row[1], float(row[2])))
        cursor.close()
        conn.close()
        return p