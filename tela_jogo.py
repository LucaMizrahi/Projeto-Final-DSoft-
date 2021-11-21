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

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

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
        # Atualizando a posição dos meteoros
        all_sprites.update()

            

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

    

        pygame.display.update()  # Mostra o novo frame para o jogador