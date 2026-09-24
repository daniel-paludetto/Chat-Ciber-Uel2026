from server_socket import create_server
from server_connection import receive

server = create_server()

print("[STARTING] server is listening...")

receive(server)