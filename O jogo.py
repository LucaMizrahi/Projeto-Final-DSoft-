# Inicialização 
# Importando as bibliotecas
import pygame
from pygame.locals import *
pygame.init()

# Tela Principal do jogo
WIDTH = 600
HEIGHT = 480
window = pygame.display.set_mode((WIDTH, HEIGHT))

fundo = pygame.image.load()  # colocar path p; imagem de fundo aqui
fundoX = 0
fundoX2 = fundo.get_width()

def puxa_janela():
    window.blit(fundo, (fundoX, 0))  
    window.blit(fundo, (fundoX2, 0))  
    pygame.display.update()  


# Inicia estrutura de dados
game = True

FPS = 30
# loop principal 
while game:
    
    puxa_janela()

    pygame.clock.tick(FPS)

    fundoX -= 1.4  # Move both background images back
    fundoX2 -= 1.4

    if fundoX < fundo.get_width() * -1:  # If our bg is at the -width then reset its position
        fundoX = fundo.get_width()
    
    if fundoX2 < fundo.get_width() * -1:
        fundoX2 = fundo.get_width()
    # Tratamento de eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    
    # Saídas 
    window.fill((255, 255, 255))
    # window.blit(())

    pygame.display.update()

pygame.quit



