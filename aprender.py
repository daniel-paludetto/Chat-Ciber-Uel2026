import pygame
from sys import exit

#fazer um comentario para testar

#mais atualizações

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) -start_time
    score_surface = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Aprendendo Pygame')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0

#tentar colocar uma imagem dps
ceu_surface = pygame.Surface((800,300))
ceu_surface.fill('Blue')

chao_surface = pygame.Surface((800,100))
chao_surface.fill('Brown')

# text_surface = test_font.render('Palmeiras', True, (64,64,64))
# text_rect = text_surface.get_rect(center = (400, 50))

obj_surface = pygame.Surface((20, 50))
obj_rect = obj_surface.get_rect(bottomright = (600, 300))
obj_surface.fill('Red')

player_surface = pygame.Surface((30, 60))
#player_x_pos = 
player_surface.fill('Pink')
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # pygame.draw.rect(screen, '#64f30b', text_rect)
        # pygame.draw.rect(screen, "#64f30b", text_rect,10)
        # #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10)
        # #pygame.draw.ellipse(screen, 'Brown1', pygame.Rect(50,200,100,100))
        # screen.blit(text_surface, text_rect)


        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True  
                obj_rect.left = 800     
                start_time = int(pygame.time.get_ticks() / 1000) 

        # if event.type == pygame.KEYUP:
        #     print('key up')


    if game_active:
        screen.blit(ceu_surface,(0,0))
        screen.blit(chao_surface,(0, 300))
        # pygame.draw.rect(screen, '#64f30b', text_rect)
        # pygame.draw.rect(screen, "#64f30b", text_rect,10)
        # #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10)
        # #pygame.draw.ellipse(screen, 'Brown1', pygame.Rect(50,200,100,100))
        # screen.blit(text_surface, text_rect)
        display_score()

        obj_rect.x -= 4
        if obj_rect.right <= 0:
            obj_rect.left = 800
        screen.blit(obj_surface, obj_rect)

        #player_rect.left += 1

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #colission 
        if obj_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # if player_rect.colliderect(obj_rect) == 1:
    #     print('colission')

    # mouse_pos  =pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    
    pygame.display.update()
    clock.tick(60)  

# Transforming Surfaces 2:05:51   
# Testando...
