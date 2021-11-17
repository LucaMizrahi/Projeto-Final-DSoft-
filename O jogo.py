# Inicialização 
# Importando as bibliotecas
import pygame
from pygame.locals import *

pygame.init()

# Tela Principal do jogo
WIDTH = 600
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Pirate')

# Inicia assets
'''player_WIDTH = ''
player_HEIGHT = ''       '''
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/img/Background.jpg').convert()
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))
#player_img = pygame.image.load('assets/img/Drunken Sailor.png').convert()
#player_img = pygame.transform.scale(player_img, ())


fundoX = 0
fundoX2 = fundo.get_width()

def puxa_janela():
    window.blit(fundo, (fundoX, 0))  
    window.blit(fundo, (fundoX2, 0))  
    pygame.display.update()  


# Inicia estrutura de dados
game = True

clock = pygame.time.Clock()
FPS = 30

# loop principal 
while game:
    
    puxa_janela()

    clock.tick(FPS)

    fundoX -= 1.4  # Move o background para trás
    fundoX2 -= 1.4

    if fundoX < fundo.get_width() * -1:  # se o width for negativo ele é resetado
        fundoX = fundo.get_width()
    
    if fundoX2 < fundo.get_width() * -1:
        fundoX2 = fundo.get_width()
    # Tratamento de eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    
    # Saídas 
    window.fill((255, 255, 255))
    window.blit(fundo, (0, 0))

    pygame.display.update()

pygame.quit



