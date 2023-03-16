# Importando bibliotecas
import pygame
import random
from classes import pirate, cannon, Button
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
    posx = (WIDTH / 2) #Posição em X
    posy = (HEIGHT / 2) #Posição em Y

    # Função utilizada para desenhar o placar do jogo
    def draw_text(text, font, text_color, x, y):
        img = assets[SCORE_FONT].render(text, True, text_color)
        window.blit(img, (x, y))

    # Função utilizada para dar reset no jogo
    def restart():
        cannon_group.empty()
        p.rect.x = 200
        p.rect.y = int(posy)
        score = 0
        return score


    # Criando grupos de sprite para o player
    sailor_group = pygame.sprite.Group()
    # Instância do player(posição na tela
    p = pirate(200, int(posy),assets)
    sailor_group.add(p)

    # Criando grupos de sprite para os canos
    cannon_group = pygame.sprite.Group()

    # Instânica do botão de restart(posição na tela e imagem)
    button = Button(posx - 100, posy - 50,assets)

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
        window.blit(assets[BACKGROUND], (mov_fundo, 0)) # Desenha o fundo

        cannon_group.draw(window) # Desenha o canhão    

        sailor_group.draw(window) # Desenha o personagem
        sailor_group.update(voando,game_over) # Atualiza o que acontece com o pirate

        # Verifica o Placar
        if len(cannon_group) > 0:
            if sailor_group.sprites()[0].rect.left > cannon_group.sprites()[0].rect.left\
                and sailor_group.sprites()[0].rect.right < cannon_group.sprites()[0].rect.right and pass_cannon == False:
                pass_cannon = True
            if (
                pass_cannon == True
                and sailor_group.sprites()[0].rect.left
                > cannon_group.sprites()[0].rect.right
            ):
                score += 1
                assets[POINT_SOUND].play()
                pass_cannon = False

        # desenha o placar na tela
        draw_text(str(score), assets[SCORE_FONT], WHITE, int(posx), 20)

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
                canhao_baixo = cannon(WIDTH, 468 + altura_canhao, -1,assets) # 488
                canhao_cima = cannon(WIDTH, 260 + altura_canhao, 1,assets) # 280
                cannon_group.add(canhao_baixo)
                cannon_group.add(canhao_cima)
                last_cannon = time_now

            # movimentação do fundo
            mov_fundo -= vel_fundo 
            if abs(mov_fundo) > 2048:
                mov_fundo = 0   

            # Atualiza o que acontece com os canhões
            cannon_group.update(vel_fundo)

        # Desenha o get ready quando o jogo está ativo porém ainda não começou(voando é Falso)
        if game_over == False and voando == False:
            window.blit(assets[GETREADY], (400, 215))                             

        # Checa por game over e restart
        if game_over == True:
            window.blit(assets[TELAGAMEOVER], (0,0)) # Desenha a tela de game over
            draw_text(str(score), assets[SCORE_FONT], WHITE, int(posx) + 60, 190) # Desenha o placar na tela de game over
            if button.draw(window) == True: # O botão foi apertado
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
