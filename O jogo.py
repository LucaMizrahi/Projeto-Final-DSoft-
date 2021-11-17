# Inicialização 
# Importando as bibliotecas
import pygame
pygame.init()

# Tela Principal do jogo
WIDTH = 600
HEIGHT = 480
window = pygame.display.set_mode((WIDTH, HEIGHT))


# Inicia estrutura de dados
game = True


# loop principal 
while game: 
    # Tratamento de eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False

    
    # Saídas 
    window.fill((255, 255, 255))
    # window.blit(())

    pygame.display.update()

pygame.quit



