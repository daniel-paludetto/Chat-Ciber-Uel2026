import threading

from config import FORMAT
from client_manager import clients, nicknames, broadcast
from client_handler import handle_client


def receive(server):
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

        thread = threading.Thread(
            target=handle_client,
            args=(client, addr)
        )

        thread.start()