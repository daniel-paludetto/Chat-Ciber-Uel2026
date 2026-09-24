clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def remove_client(client):
    index = clients.index(client)

    client.close()

    print(clients)

    nickname = nicknames[index]

    clients.remove(client)

    print(f"{nickname} desconectou do chat")

    broadcast(f"{nickname} left the chat".encode("utf-8"))

    nicknames.remove(nickname)