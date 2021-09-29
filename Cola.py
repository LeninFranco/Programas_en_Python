class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0,item)

    def desencolar(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def primero(self):
        return self.items[len(self.items)-1]

    def ultimo(self):
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)

if __name__ == "__main__":
    queue = Cola()
    queue.encolar(3)
    queue.encolar(8)
    queue.encolar(2)
    queue.encolar(1)
    queue.encolar(0)
    queue.encolar(6)
    queue.encolar(7)
    queue.encolar(5)
    print(queue)
    print(f"Primero: {queue.primero()}")
    print(f"Ultimo: {queue.ultimo()}")
    print(f"Tamaño: {queue.size()}")
    queue.desencolar()
    queue.desencolar()
    queue.desencolar()
    print("-"*30)
    print(queue)
    print(f"Primero: {queue.primero()}")
    print(f"Ultimo: {queue.ultimo()}")
    print(f"Tamaño: {queue.size()}")
