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

def isOpen(character):
    return character in ('(','[','{')

def closes(topeChar,character):
    pares = {'(':')','[':']','{':'}'}
    return pares[topeChar] == character


def balanceo(text):
    stack = Pila()
    for char in text:
        if isOpen(char):
            stack.push(char)
        else:
            tope = stack.pop()
            if not closes(tope,char):
                return False
    return True

if __name__ == "__main__":
    print(balanceo("(())"))
    print(balanceo("({()()}[()])"))
    print(balanceo("{[}()]"))