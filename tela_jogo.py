import pygame
import random
from pygame.locals import *
from configuracoes import *
from assets import *


def game_screen(window):
    # Inicialização 
    # Importando as bibliotecas

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
    score = 0
    # Gatilho que eh acionado quando o pirata passa um canhao, para auxiliar na contagem do placar:
    passou_canhao = False

    # ===== Loop principal =====
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