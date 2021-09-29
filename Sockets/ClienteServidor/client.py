import socket
import json

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    if msg != "":
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        print(client.recv(2048).decode(FORMAT))

def readList():
    msg = []
    for i in range(3):
        var = input("->")
        if var == DISCONNECT_MESSAGE:
            return var
        msg.append(var)
    return json.dumps(msg)

while True:
    msg = input("->")
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        client.close()
        break