#modulo da interfacee
import pygame

AZUL = (1, 36, 86)
BRANCO = (245, 247, 250)

LARGURA, ALTURA = 800, 600
tela = None
fonte = None
relogio = None
altura_linha = 0
y_input = 0

def inicializar_interface():
    global tela, fonte, relogio, altura_linha, y_input
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("WhatsApp 2.0 :D")
    relogio = pygame.time.Clock()
    
    fonte = pygame.font.SysFont("consolas", 24)
    altura_linha = fonte.get_linesize()
    y_input = ALTURA - altura_linha - 20

def desenhar_tela_nickname(nickname):
    tela.fill(AZUL)
    
    titulo = fonte.render("Whatsapp 2.0", True, BRANCO)
    tela.blit(titulo, (300, 150))
    
    texto = fonte.render("Digite seu nickname:", True, BRANCO)
    tela.blit(texto, (250, 250))

    nickname_surf = fonte.render(f"> {nickname}", True, BRANCO)
    tela.blit(nickname_surf, (250, 310))

    instrucao = fonte.render("Pressione ENTER para continuar", True, BRANCO)
    tela.blit(instrucao, (200, 400))

    pygame.display.flip()

def desenhar_tela_chat(lista_mensagens, texto_digitado):
    tela.fill(AZUL)

    y_atual = y_input - altura_linha
    for msg in reversed(lista_mensagens):
        if y_atual < 0:
            break
        msg_surf = fonte.render(msg, True, BRANCO)
        tela.blit(msg_surf, (10, y_atual))
        y_atual -= altura_linha

    texto_surf = fonte.render(f"> {texto_digitado}", True, BRANCO)
    tela.blit(texto_surf, (10, y_input))

    pygame.display.flip()

def controlar_fps(fps=60):
    relogio.tick(fps)

def encerrar_interface():
    pygame.quit()

