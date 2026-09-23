#cliente

import socket
import threading
import pygame

nickname = input("Choose a nickname: ")

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDR)
    conectado = True
    
except:
    print("Erro ao conectar com o servidor")
    conectado = False

pygame.init()

LARGURA, ALTURA = 800, 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("WhatsApp 2.0 :D")

relogio = pygame.time.Clock()

AZUL = ('#012456')
BRANCO = ("#F5F7FA")

fonte = pygame.font.SysFont("consolas", 24)
altura_linha = fonte.get_linesize()

mensagens = []
texto_digitado = ""

y_input = ALTURA - altura_linha - 20

def receive():
    while conectado:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
            else:
                mensagens.append(message)
        except:
            print("An error occurred")
            client.close()
            break

def send(message):
    try:
        message = message.encode(FORMAT)
        msg_length = str(len(message)).encode(FORMAT)
        msg_length += b' ' * (HEADER - len(msg_length))
        client.send(msg_length)
        client.send(message)
    except:   
        pass
 
if conectado:
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

while conectado:
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            conectado = False
            
        elif evento.type == pygame.KEYDOWN:
            
            #ENTER
            if evento.key == pygame.K_RETURN:
                
                if texto_digitado.strip() != "":
                    msg = f"{nickname}: {texto_digitado}"
                    send(msg)
                    texto_digitado = ""
            
            #BACKSPACE
            elif evento.key == pygame.K_BACKSPACE:
                texto_digitado = texto_digitado[:-1]
                
            elif evento.key == pygame.K_ESCAPE:
                conectado = False
            
            #TEXTO DIGITADO
            else:
                if evento.unicode.isprintable():
                    texto_digitado += evento.unicode

    #GERENCIAMENTO DE MEMORIA                
    max_mensagens = y_input
    while len(mensagens) > max_mensagens:
        mensagens.pop()

    #DESENHO NA TELA
    tela.fill(AZUL)

    y_atual = y_input - altura_linha
    for msg in reversed(mensagens):
        msg_superficie = fonte.render(msg, True, BRANCO)
        tela.blit(msg_superficie, (10, y_atual))
        y_atual -= altura_linha

    texto_superficie = fonte.render(f"> {texto_digitado}", True, BRANCO)
    tela.blit(texto_superficie, (10, y_input))

    pygame.display.flip()

    relogio.tick(60)

#DESCONECTAR
if client:
    try:
        send(DISCONNECT_MESSAGE)
    except:
        pass
    
    finally:
        conectado = False
        client.close()

pygame.quit()
                    
                    
