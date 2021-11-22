# Inicialização 
# Importando as bibliotecas
import pygame
from configuracoes import *
from pygame.locals import *
from tela_inicial import init_screen
from tela_jogo import game_screen

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Sailor')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# Tela Principal do jogo
WIDTH = 1024
HEIGHT = 768
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Sailor')

mov_fundo = 0 
vel_fundo = 4 # Velocidade de movimentação do fundo
freq_cannon = 1500 #Milisegundos
last_cannon = pygame.time.get_ticks()

'''player_WIDTH = ''
player_HEIGHT = ''       '''
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('Assets/img/padrao_pirata.png').convert()
#player_img = pygame.image.load('assets/img/Drunken Sailor.png').convert()
#player_img = pygame.transform.scale(player_img, ())







# Inicia estrutura de dados
game = True

clock = pygame.time.Clock()
FPS = 60

# loop principal 
while game:
    
    #puxa_janela()

    clock.tick(FPS)

    # Tratamento de eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    
    # Saídas 
    window.blit(fundo, (mov_fundo, 0)) # Desenha o fundo
    mov_fundo -= vel_fundo # movimentação do fundo

    sailor_group.draw(window) # Desenha o personagem

    cannon_group.draw(window) # Desenha o canhão    

    if abs(mov_fundo) > 2048:
        mov_fundo = 0

    pygame.display.update()

pygame.quit()



