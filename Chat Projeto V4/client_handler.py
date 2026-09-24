from config import HEADER, FORMAT, DISCONNECT_MESSAGE
from client_manager import broadcast, remove_client


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