import pygame
import random
from os import path
from configuracoes import *
from pygame.locals import *
from tela_inicial import init_screen
from tela_jogo import game_screen

cannon_group = pygame.sprite.Group()
p = pirate(200, int(HEIGHT / 2))

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Sailor')
font = pygame.font.SysFont('Bauhaus 93', 48)
fundo = pygame.image.load('assets/img/padrao_pirata.png').convert()
button_img = pygame.image.load('assets/img/button.png')

def restart():
    cannon_group.empty()
    p.rect.x = 200
    p.rect.y = int(HEIGHT / 2)
    score = 0
    return score


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

button = Button((WIDTH / 2) - 50, (HEIGHT / 2) - 100, button_img)

def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, '.png')).convert_alpha()
    background_set = pygame.transform.scale(background, (WIDTH,HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == button.draw():
                game_over = False
                score = restart()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background_set, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


