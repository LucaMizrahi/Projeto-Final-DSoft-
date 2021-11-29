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
    assets = {}
    assets['background'] = pygame.image.load('assets/img/padrao_pirata.png').convert()
    assets['pirate'] = pygame.image.load('Assets/img/Drunken_Sailor.png').convert_alpha()
    assets['pirate'] = pygame.transform.scale(assets['pirate'], (70, 70))
    assets['cannon'] = pygame.image.load('assets/img/cano1.png').convert_alpha()
    assets['button'] = pygame.image.load('assets/img/button.png')
    assets['game_over'] = pygame.image.load('assets/img/gameover.png').convert_alpha()
    assets['game_over'] = pygame.transform.scale(assets['game_over'], (364, 100))
    assets['get_ready'] = pygame.image.load('assets/img/getready.png').convert_alpha()
    assets['get_ready'] = pygame.transform.scale(assets['get_ready'], (210, 223))
    assets['tela_gameover'] = pygame.image.load('assets/img/telagameover.png').convert()
    assets['tela_gameover'] = pygame.transform.scale(assets['tela_gameover'], (WIDTH, HEIGHT))

    # Carrega os sons
    pygame.mixer.music.load('assets/audios/theme.wav')
    pygame.mixer.music.set_volume(0.3)
    assets['die_sound'] = pygame.mixer.Sound('assets/audios/crash.wav')
    assets['point_sound'] = pygame.mixer.Sound('assets/audios/point.wav')

    # Carrega fonte
    assets['score_font'] = pygame.font.Font(('assets/fontes/PressStart2P.ttf'), 28)

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
            self.image = assets['pirate']
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
            self.image = assets['cannon']
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
    while state != DONE:
        clock.tick(FPS)

        # Conta o placar:
        if len(all_cannons) > 0:
            if player.rect.left > all_cannons.sprites()[0].rect.left and player.rect.right < all_cannons.sprites()[0].rect.right and passou_canhao == False:
                passou_canhao = True
            if passou_canhao == True:
                if player.rect.left > all_cannons.sprites()[0].rect.right:
                    score += 1
                    passou_canhao = False




        # Verifica se houve colisão entre pirata e canhao ou pirata e chao:
        if player.rect.bottom >= 768:
            state = DONE

        if pygame.sprite.spritecollide(player, all_cannons, False, pygame.sprite.collide_mask):
            state = DONE
            assets[CRASH_SOUND].play()
            player.kill()
            keys_down = {}

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if event.type == pygame.KEYDOWN:
                if state == PLAYING:
                        if event.key == pygame.K_SPACE:
                            player.jump()

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos canhoes
        all_sprites.update()

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        # all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

    

        pygame.display.update()  # Mostra o novo frame para o jogador
