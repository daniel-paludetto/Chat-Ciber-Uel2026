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

def quebrar_texto(texto, largura_max):
    linhas = []
    atual = ""
    for palavra in texto.split(" "):
        candidato = palavra if atual == "" else atual + " " + palavra
        if fonte.size(candidato)[0] <= largura_max:
            atual = candidato
        elif atual and fonte.size(palavra)[0] <= largura_max:
            linhas.append(atual)
            atual = palavra
        else:
            if atual:
                atual += " "
            for c in palavra:
                if fonte.size(atual + c)[0] <= largura_max:
                    atual += c
                else:
                    linhas.append(atual)
                    atual = c
    linhas.append(atual)
    return linhas

def desenhar_tela_chat(lista_mensagens, texto_digitado):
    tela.fill(AZUL)
    largura_max = LARGURA - 20
    
    linhas_input = quebrar_texto(f"> {texto_digitado}", largura_max)
    y_topo_input = ALTURA - 20 - len(linhas_input) * altura_linha
    
    for i, linha in enumerate(linhas_input):
        surf = fonte.render(linha, True, BRANCO)
        tela.blit(surf, (10, y_topo_input + i * altura_linha))
    y_atual = y_topo_input
    
    y_atual = y_topo_input
    for msg in reversed(lista_mensagens):
        linhas = quebrar_texto(msg, largura_max)
        y_atual -= len(linhas) * altura_linha
        for i, linha in enumerate(linhas):
            surf = fonte.render(linha, True, BRANCO)
            tela.blit(surf, (10, y_atual + i * altura_linha))
        if y_atual < 0:
            break

    pygame.display.flip()

def controlar_fps(fps=60):
    relogio.tick(fps)

def encerrar_interface():
    pygame.quit()

