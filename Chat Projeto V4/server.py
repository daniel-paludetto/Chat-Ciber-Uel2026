#server

import socket
import threading

from config import HEADER, PORT, SERVER, ADDR, FORMAT, DISCONNECT_MESSAGE
#server

import socket
import threading

from config import HEADER, PORT, SERVER, ADDR, FORMAT, DISCONNECT_MESSAGE
from client_manager import clients, nicknames, broadcast, remove_client

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

def remove_client(client): ...
def broadcast(message): ...


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_client(client, addr):
    connected = True
    while connected:
        try:
            msg_length = client.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = client.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    remove_client(client)
                    break
                broadcast(msg.encode(FORMAT))

        except:
            remove_client(client)
            break
    client.close()


def receive():
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send("NICK".encode(FORMAT))
        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode(FORMAT))
        client.send("Connected to the server".encode(FORMAT))

        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()


print("[STARTING] server is listening...")
receive()
