import socket

from config import ADDR


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(ADDR)

    server.listen()

    return server