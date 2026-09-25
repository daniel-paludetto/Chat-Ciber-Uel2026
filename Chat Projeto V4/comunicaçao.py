#modulo que isola a comunicacao em rede
import socket
import threading
import interface 
from config import HEADER, PORT, SERVER, FORMAT, DISCONNECT_MESSAGE

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conectado = False
mensagens = []

def conectar():
    global conectado
    try:
        client.connect((SERVER, PORT))
        conectado = True
        return True
    except Exception as e:
        print(f"Erro ao conectar com o servidor: {e}")
        conectado = False
        return False

def receber(obter_nickname):
    global conectado
    while conectado:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                nickname = obter_nickname()
                client.send(nickname.encode(FORMAT))
            else:
                mensagens.append(message)
        except:
            print("Conexão perdida com o servidor.")
            fechar_conexao()
            break

def iniciar_receber(obter_nickname):
    if conectado:
        thread = threading.Thread(target=receber, args=(obter_nickname,), daemon=True)
        thread.start()

def mandar(mensagem):
    if not conectado:
        return
    try:
        msg_encoded = mensagem.encode(FORMAT)
        msg_length = str(len(msg_encoded)).encode(FORMAT)
        msg_length += b' ' * (HEADER - len(msg_length))
        client.send(msg_length)
        client.send(msg_encoded)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def desconectar():
    if conectado:
        mandar(DISCONNECT_MESSAGE)
        fechar_conexao()

def fechar_conexao():
    global conectado
    conectado = False
    try:
        client.close()
    except:
        pass