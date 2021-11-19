# Inicialização 
# Importando as bibliotecas
import pygame
from pygame.locals import *

pygame.init()

# Tela Principal do jogo
WIDTH = 1024
HEIGHT = 768
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Pirate')

mov_fundo = 0 
vel_fundo = 4 # Velocidade de movimentação do fundo

'''player_WIDTH = ''
player_HEIGHT = ''       '''
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/img/padrao_pirata.png').convert()
#player_img = pygame.image.load('assets/img/Drunken Sailor.png').convert()
#player_img = pygame.transform.scale(player_img, ())

class sailor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/img/Drunken Sailor.png').convert_alpha()
        # self.image = pygame.transform.scale(self.image, (110,110))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
class canhao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/img/Cannon.png').convert_alpha()
        #self.image = pygame.transform.scale(self.image, (110,110))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


sailor_group = pygame.sprite.Group()
cannon_group = pygame.sprite.Group()

s = sailor(200, int(HEIGHT / 2))
c = canhao(800, 628)

sailor_group.add(s)
cannon_group.add(c)



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

pygame.quit



