class Producto:
    def __init__(self,ID:str,nombre:str,precio:float):
        self.ID = ID
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return "ID: " + self.ID + "\nNombre: " + self.nombre + "\nPrecio: $" + str(self.precio) + "\n"