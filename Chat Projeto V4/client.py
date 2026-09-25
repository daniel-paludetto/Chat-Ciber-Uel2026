
import pygame
import interface
import comunicaçao

def main():
    interface.inicializar_interface()
    
    if not comunicaçao.conectar():
        print("Não foi possível conectar ao servidor. Encerrando...")
        interface.encerrar_interface()
        return

    nickname = ""
    texto_digitado = ""
    tela_atual = "nickname"

    rodando = True
    while rodando and comunicaçao.conectar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            elif evento.type == pygame.KEYDOWN:
                if tela_atual == "nickname":
                    if evento.key == pygame.K_RETURN:
                        if nickname.strip() != "":
                            tela_atual = "chat"
                            comunicaçao.iniciar_receber(lambda: nickname) #labda cria funcoes sem nome(mais ideal pra coisas simples)
                    elif evento.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    elif evento.unicode.isprintable() and len(nickname) < 20:
                        nickname += evento.unicode

                elif tela_atual == "chat":
                    if evento.key == pygame.K_RETURN:
                        if texto_digitado.strip() != "":
                            msg = f"{nickname}: {texto_digitado}"
                            comunicaçao.mandar(msg)
                            texto_digitado = ""
                    elif evento.key == pygame.K_BACKSPACE:
                        texto_digitado = texto_digitado[:-1]
                    elif evento.key == pygame.K_ESCAPE:
                        rodando = False
                    elif evento.unicode.isprintable():
                        texto_digitado += evento.unicode

        if tela_atual == "nickname":
            interface.desenhar_tela_nickname(nickname)
        elif tela_atual == "chat":
            interface.desenhar_tela_chat(comunicaçao.mensagens, texto_digitado)

        interface.controlar_fps(60)

    comunicaçao.desconectar()
    interface.encerrar_interface()

if __name__ == "__main__":
    main()