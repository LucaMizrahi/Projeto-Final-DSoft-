# Importando bibliotecas
import pygame
import random
from pygame.locals import *
from configuracoes import *
from assets import *


def game_screen(window):

    pygame.init()
    pygame.mixer.init()

    # Tela Principal do jogo
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Drunken Sailor')

    # Inicia assets
    assets = load_assets()
    
    # Define variáveis
    mov_fundo = 0 
    vel_fundo = 4 # Velocidade de movimentação do fundo
    voando = False
    game_over = False
    freq_cannon = 1500 
    last_cannon = pygame.time.get_ticks() - freq_cannon
    score = 0 
    pass_cannon = False

    # Função utilizada para desenhar o placar do jogo
    def draw_text(text, font, text_color, x, y):
        img = assets[SCORE_FONT].render(text, True, text_color)
        window.blit(img, (x, y))

    # Função utilizada para dar reset no jogo
    def restart():
        cannon_group.empty()
        p.rect.x = 200
        p.rect.y = int(HEIGHT / 2)
        score = 0
        return score


    # DEFINE CLASSES
    class pirate(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets[PIRATE]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            self.vel = 0
            self.click = False
        
        def update(self):
            
            # Gravidade
            if voando == True:
                self.vel += 0.5
                if self.vel > 8 :
                    self.vel = 8
                if self.rect.bottom < 768:
                    self.rect.y += int(self.vel)

            if game_over == False:
                # Pulo 
                if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                    self.click = True
                    self.vel = -10
                if pygame.mouse.get_pressed()[0] == 0:
                    self.click = False

    # Criando grupos de sprite para o player
    sailor_group = pygame.sprite.Group()
    # Instância do player(posição na tela
    p = pirate(200, int(HEIGHT / 2))
    sailor_group.add(p)

    class cannon(pygame.sprite.Sprite):
        def __init__(self, x, y, posicao):
            pygame.sprite.Sprite.__init__(self)
            self.image = assets[CANNON]
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect()

            # A posição 1 equivale ao cano vindo de cima e -1 ao cano vindo de baixo
            if posicao == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y]
            if posicao == -1:
                self.rect.topleft = [x, y]
        
        def update(self):
            self.rect.x -= vel_fundo

            # Tira os canhões que já passaram pela tela
            if self.rect.right < 0:
                self.kill() 

    # Criando grupos de sprite para os canos
    cannon_group = pygame.sprite.Group()

    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)

        def draw(self):
            action = False
            
            # Ver a posição do mouse
            posicao = pygame.mouse.get_pos()

            # Checa se o mouse está em cima do botão
            if self.rect.collidepoint(posicao):
                if pygame.mouse.get_pressed()[0] == 1: # Botão esquerda do mouse foi pressionado
                    action = True

            # Desenha botão
            window.blit(self.image, (self.rect.x, self.rect.y))
            return action

    # Instânica do botão de restart(posição na tela e imagem)
    button = Button((WIDTH / 2) - 50, (HEIGHT / 2) - 100, assets['button'])



    # Inicia estrutura de dados
    game = True

    # Define os frames por segundo
    clock = pygame.time.Clock()
    FPS = 60

    # Toca a música do jogo
    pygame.mixer.music.play(loops=-1)
    # loop principal 
    while game:

        clock.tick(FPS)

        # Saídas 
        window.blit(assets['background'], (mov_fundo, 0)) # Desenha o fundo

        cannon_group.draw(window) # Desenha o canhão    

        sailor_group.draw(window) # Desenha o personagem
        sailor_group.update() # Atualiza o que acontece com o pirate
        
        # Verifica o Placar
        if len(cannon_group) > 0:
            if sailor_group.sprites()[0].rect.left > cannon_group.sprites()[0].rect.left\
                and sailor_group.sprites()[0].rect.right < cannon_group.sprites()[0].rect.right and pass_cannon == False:
                pass_cannon = True
            if pass_cannon == True:
                if sailor_group.sprites()[0].rect.left > cannon_group.sprites()[0].rect.right:
                    score += 1
                    assets['point_sound'].play()
                    pass_cannon = False

        # desenha o placar na tela
        draw_text(str(score), assets['score_font'], WHITE, int(WIDTH / 2), 20)

        # Checa se o pirata bateu no canhão ou no teto
        if pygame.sprite.groupcollide(sailor_group, cannon_group, False, False) or p.rect.top < 0: # Os bol indicam que algum dos grupos seria deletado caso fosse atingido
            game_over = True

        # Checa se o pirata bateu no chão
        if p.rect.bottom >= 768:
            game_over = True
            voando = False

        # Checa se o jogo ainda não acabou
        if game_over == False and voando == True: 
            # Gerar novos canhões
            time_now = pygame.time.get_ticks()
            if time_now - last_cannon > freq_cannon:
                altura_canhao = random.randint(-100, 100)
                canhao_baixo = cannon(WIDTH, 468 + altura_canhao, -1) # 488
                canhao_cima = cannon(WIDTH, 260 + altura_canhao, 1) # 280
                cannon_group.add(canhao_baixo)
                cannon_group.add(canhao_cima)
                last_cannon = time_now

            # movimentação do fundo
            mov_fundo -= vel_fundo 
            if abs(mov_fundo) > 2048:
                mov_fundo = 0   

            # Atualiza o que acontece com os canhões
            cannon_group.update()

        # Desenha o get ready quando o jogo está ativo porém ainda não começou(voando é Falso)
        if game_over == False and voando == False:
            window.blit(assets['get_ready'], (400, 215))                             

        # Checa por game over e restart
        if game_over == True:
            window.blit(assets['tela_gameover'], (0,0)) # Desenha a tela de game over
            draw_text(str(score), assets['score_font'], WHITE, int(WIDTH / 2) + 60, 190) # Desenha o placar na tela de game over
            if button.draw() == True: # O botão foi apertado
                game_over = False
                score = restart()

        # Tratamento de eventos para definir se o jogo deve acabar e se o personagem deve começar a voar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN and voando == False and game_over == False:
                voando = True
        

        pygame.display.update()

    pygame.quit
