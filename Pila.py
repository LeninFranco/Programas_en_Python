class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

if __name__ == "__main__":
    stack = Pila()
    stack.push(2)
    stack.push(1)
    stack.push(5)
    stack.push(4)
    stack.push(9)
    stack.push(6)
    stack.push(7)
    print(stack)
    print(f"Tope: {stack.top()}")
    print(f"Tamaño: {stack.size()}")
    print("-"*30)
    stack.pop()
    stack.pop()
    print(stack)
    print(f"Tope: {stack.top()}")
    print(f"Tamaño: {stack.size()}")
