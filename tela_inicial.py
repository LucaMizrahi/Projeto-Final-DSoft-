# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 400

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Sailor')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('Assets/img/First_screen.png').convert_alpha()
background_set = pygame.transform.scale(image, (WIDTH,HEIGHT))
font = pygame.font.SysFont(None, 50)
text = font.render('Drunken Sailor', True, (0, 0, 0))
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.blit(background_set, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados