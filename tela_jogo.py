import pygame
from configuracoes import *
from assets import *
from sprites import *


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_cannons = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_cannons'] = all_cannons

    # Criando o jogador
    player = pirate(groups, assets)
    all_sprites.add(player)
    # Criando os meteoros
    for i in range(8):
        cannon = cannon(assets)
        all_sprites.add(cannon)
        all_cannons.add(cannon)

    DONE = 0
    PLAYING = 1
    state = PLAYING

    score = 0
    # Gatilho que eh acionado quando o pirata passa um canhao, para auxiliar na contagem do placar:
    passou_canhao = False

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # Conta o placar:
        if len(all_cannons) > 0:
            if pirate.rect.left > all_cannons.sprites()[0].rect.left and pirate.rect.right < all_cannons.sprites()[0].rect.right and passou_canhao == False:
                passou_canhao = True
            if passou_canhao == True:
                if pirate.rect.left > all_cannons.sprites()[0].rect.right:
                    score += 1
                    passou_canhao = False




        # Verifica se houve colisão entre pirata e canhao ou pirata e chao:
        if pirate.rect.bottom >= 768:
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
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

    

        pygame.display.update()  # Mostra o novo frame para o jogador