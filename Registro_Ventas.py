import os

productos = {}
ventas = {}
N_Venta = 1

def isInteger(var):
    try:
        int(var)
        return True
    except:
        return False

def isFloat(var):
    try:
        float(var)
        return True
    except:
        return False

def MenuSeleccion():
    while(True):
        os.system("cls")
        print("******************************")
        print("*   Seleccione un Registro   *")
        print("******************************")
        print("* 1. Registro de Productos   *")
        print("* 2. Registro de Ventas      *")
        print("******************************")
        opc = input(">>> ")
        if(not isInteger(opc)):
            continue
        elif(int(opc)<1 or int(opc)>2):
            continue
        else:
            return int(opc)
            break

class Producto:
    def __init__(self, identificador, nombre, precio):
        self.ID = identificador
        self.Nombre = nombre
        self.Precio = precio
    def getID(self):
        return self.ID
    def getNombre(self):
        return self.Nombre
    def getPrecio(self):
        return self.Precio

class Venta:
    def __init__(self, producto, cantidad):
        global N_Venta
        self.NVenta = N_Venta
        N_Venta += 1
        self.producto = producto.getNombre()
        self.precioUnit = producto.getPrecio()
        self.cantidad = cantidad
        self.total = cantidad * producto.getPrecio()
    def getNVenta(self):
        return self.NVenta
    def getProducto(self):
        return self.producto
    def getPrecioUnitario(self):
        return self.precioUnit
    def getCantidad(self):
        return self.cantidad
    def getTotal(self):
        return self.total

class RegistroProductos:
    @staticmethod
    def addProducto(producto):
        productos[producto.getID()] = producto
    @staticmethod
    def removeProducto(ID):
        del(productos[ID])
    @staticmethod
    def updateProducto(producto):
        productos[producto.getID()] = producto
    @staticmethod
    def searchProducto(ID):
        fila = productos[ID]
        print("{:<10} {:<35} {:<25}".format("ID","Producto","Precio Unitario"))
        print("-"*65)
        print("{:<10} {:<35} {:<25}".format(fila.getID(),fila.getNombre(),fila.getPrecio()))
    @staticmethod
    def selectAll():
        print("{:<10} {:<35} {:<25}".format("ID","Producto","Precio Unitario"))
        print("-"*65)
        for i in productos.keys():
            fila = productos[i]
            print("{:<10} {:<35} {:<25}".format(fila.getID(),fila.getNombre(),fila.getPrecio()))
            print("-"*65)

class RegistroVentas:
    @staticmethod
    def addVenta(venta):
        ventas[venta.getNVenta()] = venta
    @staticmethod
    def removeVenta(NumVenta):
        del(ventas[NumVenta])
    @staticmethod
    def updateVenta(venta):
        ventas[venta.getNVenta()] = venta
    @staticmethod
    def searchVenta(NumVenta):
        fila = ventas[NumVenta]
        print("{:<15} {:<35} {:<20} {:<15} {:<15}".format("NumVenta","Producto","Precio Unitario","Cantidad","Total"))
        print("-"*95)
        print("{:<15} {:<35} {:<20} {:<15} {:<15}".format(fila.getNVenta(),fila.getProducto(),fila.getPrecioUnitario(),fila.getCantidad(),fila.getTotal()))
    @staticmethod
    def selectAll():
        print("{:<15} {:<35} {:<20} {:<15} {:<15}".format("NumVenta","Producto","Precio Unitario","Cantidad","Total"))
        print("-"*95)
        for i in ventas.keys():
            fila = ventas[i]
            print("{:<15} {:<35} {:<20} {:<15} {:<15}".format(fila.getNVenta(),fila.getProducto(),fila.getPrecioUnitario(),fila.getCantidad(),fila.getTotal()))
            print("-"*95)



if __name__ == "__main__":    
    print("Hola Mundo)
