import os

class Cuenta:
    def __init__(self, numeroCuenta, saldo):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
    def depositar(self, monto):
        self.saldo += monto
    def retirar(self,monto):
        self.saldo -= monto
    def __str__(self):
        return f"Numero de Cuenta: {self.numeroCuenta}\nSaldo: ${self.saldo:,}"

class Cliente:
    def __init__(self, cuenta, nombre, apellido):
        self.cuenta = cuenta
        self.nombre = nombre
        self.apellido = apellido
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellido
    def __str__(self):
        return f"Nombre Completo: {self.getNombreCompleto()}\n{self.cuenta}"

class Banco:
    def __init__(self):
        self.datasource = {}
    def addCliente(self, cliente):
        self.datasource[cliente.cuenta.numeroCuenta] = cliente
    def deleteCliente(self, numeroCuenta ):
        if(numeroCuenta in self.datasource.keys()):
            del(self.datasource[numeroCuenta])
    def searchCliente(self, numeroCuenta):
        if(numeroCuenta in self.datasource.keys()):
            return self.datasource[numeroCuenta]
        return None
    def printDataSource(self):
        print("{:<7} {:<18} {:<15}".format("Cuenta","Nombre Completo", "Saldo"))
        for key in self.datasource.keys():
            c = self.datasource[key]
            print("{:<7} {:<18} {:<15}".format(c.cuenta.numeroCuenta,c.getNombreCompleto(),c.cuenta.saldo))


if __name__ == "__main__":
    banco = Banco()
    banco.addCliente(Cliente(Cuenta(1787,6600),"Lenin","Franco"))
    banco.addCliente(Cliente(Cuenta(3038,3450),"Armando","Lopez"))
    banco.addCliente(Cliente(Cuenta(8592,19720),"Victoria","Ramirez"))
    banco.addCliente(Cliente(Cuenta(1253,3200),"Patricia","Chavez"))
    banco.addCliente(Cliente(Cuenta(9271,5000),"Pedro","Aguilar"))
    banco.printDataSource()
    print("\nOperaciones:")
    print("\nRetiro")
    banco.searchCliente(1787).cuenta.retirar(600)
    banco.searchCliente(1253).cuenta.depositar(600)
    print(banco.searchCliente(1787))
    print("\nDeposito")
    print(banco.searchCliente(1253))