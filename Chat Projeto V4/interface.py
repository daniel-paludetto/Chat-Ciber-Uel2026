import pygame

FUNDO = (26, 27, 38)
TEXTO = (192, 202, 245)
SUAVE = (86, 95, 137)
DESTAQUE = (122, 162, 247)
CORES_NOMES = [
    (122, 162, 247),
    (187, 154, 247),
    (158, 206, 106),
    (224, 175, 104),
    (247, 118, 142),
    (125, 207, 255),
]

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
    tela.fill(FUNDO)
    
    titulo = fonte.render("Whatsapp 2.0", True, DESTAQUE)
    tela.blit(titulo, (300, 150))
    
    texto = fonte.render("Digite seu nickname:", True, TEXTO)
    tela.blit(texto, (250, 250))

    nickname_surf = fonte.render(f"> {nickname}", True, TEXTO)
    tela.blit(nickname_surf, (250, 310))

    instrucao = fonte.render("Pressione ENTER para continuar", True, SUAVE)
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

def cor_do_nome(nome):
    return CORES_NOMES[sum(ord(c) for c in nome) % len(CORES_NOMES)]

def desenhar_mensagem(msg, y, largura_max):
    linhas = quebrar_texto(msg, largura_max)
    if ": " in msg:
        nome = msg.split(": ", 1)[0]
        prefixo = len(nome) + 2
        cor_nome, cor_texto = cor_do_nome(nome), TEXTO
    else:
        prefixo, cor_nome, cor_texto = 0, SUAVE, SUAVE
    for i, linha in enumerate(linhas):
        x = 10
        yy = y + i * altura_linha
        if i == 0 and prefixo:
            n = min(prefixo, len(linha))
            parte_nome = fonte.render(linha[:n], True, cor_nome)
            tela.blit(parte_nome, (x, yy))
            x += parte_nome.get_width()
            linha = linha[n:]
        if linha:
            tela.blit(fonte.render(linha, True, cor_texto), (x, yy))
    return len(linhas)

def desenhar_tela_chat(lista_mensagens, texto_digitado):
    tela.fill(FUNDO)
    largura_max = LARGURA - 20

    linhas_input = quebrar_texto(f"> {texto_digitado}", largura_max)
    y_topo_input = ALTURA - 20 - len(linhas_input) * altura_linha
    for i, linha in enumerate(linhas_input):
        yy = y_topo_input + i * altura_linha
        if i == 0:
            prompt = fonte.render("> ", True, DESTAQUE)
            tela.blit(prompt, (10, yy))
            tela.blit(fonte.render(linha[2:], True, TEXTO), (10 + prompt.get_width(), yy))
        else:
            tela.blit(fonte.render(linha, True, TEXTO), (10, yy))

    pygame.draw.line(tela, SUAVE, (10, y_topo_input - 6), (LARGURA - 10, y_topo_input - 6), 1)

    y_atual = y_topo_input - 12
    for msg in reversed(lista_mensagens):
        n_linhas = len(quebrar_texto(msg, largura_max))
        y_atual -= n_linhas * altura_linha
        desenhar_mensagem(msg, y_atual, largura_max)
        if y_atual < 0:
            break

    pygame.display.flip()

def controlar_fps(fps=60):
    relogio.tick(fps)

def encerrar_interface():
    pygame.quit()
 