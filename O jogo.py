# Inicialização 
# Importando as bibliotecas
import pygame
import random
from configuracoes import *
from pygame.locals import *
from tela_inicial import init_screen
from tela_jogo import game_screen

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drunken Sailor')
font = pygame.font.SysFont('Bauhaus 93', 48)
fundo = pygame.image.load('assets/img/padrao_pirata.png').convert()
button_img = pygame.image.load('assets/img/button.png')

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

# Define variáveis
mov_fundo = 0 
vel_fundo = 4 # Velocidade de movimentação do fundo
freq_cannon = 1500 #Milisegundos
last_cannon = pygame.time.get_ticks() - freq_cannon
voando = False
game_over = False
score = 0 
pass_cannon = False


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x, y))

def restart():
    cannon_group.empty()
    p.rect.x = 200
    p.rect.y = int(HEIGHT / 2)
    score = 0
    return score

class pirate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/img/Drunken_Sailor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.click = False
    
    def update(self):
        
        # Gravidade
        if voando == True:
            self.vel += 0.5
            if self.vel > 8 :
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over == False:
            # Pulo 
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False


        # Rotação do Pirata
        # self.image = pygame.transform.rotate(self.image, self.vel * -2)
        

        
class cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/img/Cannon.png').convert_alpha()
        #self.image = pygame.transform.scale(self.image, (110,110))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # A posição 1 equivale a imagem vindo de cima e -1 a imagem vindo de baixo
        if posicao == 1:
            self.image = pygame.transform.flip(self.image, False, True) # O primeiro bol equivale ao eixo x e o segundo ao eixo y
            self.rect.bottomleft = [x, y]
        if posicao == -1:
            self.rect.topleft = [x, y]
    
    def update(self):
        self.rect.x -= vel_fundo

        # Tira os canhões que já passaram pela tela
        if self.rect.right < 0:
            self.kill() 

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

# Cria grupos 
sailor_group = pygame.sprite.Group()
cannon_group = pygame.sprite.Group()

p = pirate(200, int(HEIGHT / 2))
sailor_group.add(p)

# Instânica do botão de restart
button = Button((WIDTH / 2) - 50, (HEIGHT / 2) - 100, button_img)




# Inicia estrutura de dados
game = True

clock = pygame.time.Clock()
FPS = 60

# loop principal 
while game:
    
    #puxa_janela()

    clock.tick(FPS)

    # Saídas 
    window.blit(fundo, (mov_fundo, 0)) # Desenha o fundo

    cannon_group.draw(window) # Desenha o canhão    

    sailor_group.draw(window) # Desenha o personagem
    sailor_group.update() # Atualiza o que acontece com o pirate

    # Verifica o Placar
    if len(cannon_group) > 0:
        if sailor_group.sprites()[0].rect.left > cannon_group.sprites()[0].rect.left\
            and sailor_group.sprites()[0].rect.right < cannon_group.sprites()[0].rect.right and pass_cannon == False:
            pass_cannon = True
        if pass_cannon == True:
            if sailor_group.sprites()[0].rect.left > cannon_group.sprites()[0].rect.right:
                score += 1
                pass_cannon = False
        
    draw_text(str(score), font, WHITE, int(WIDTH / 2), 20)

    # Checa se o pirata bateu no canhão
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
            canhao_baixo = cannon(WIDTH, 468 + altura_canhao, -1) # 488
            canhao_cima = cannon(WIDTH, 260 + altura_canhao, 1)  # 280
            cannon_group.add(canhao_baixo)
            cannon_group.add(canhao_cima)
            last_cannon = time_now

        # movimentação do fundo
        mov_fundo -= vel_fundo 
        if abs(mov_fundo) > 2048:
            mov_fundo = 0
        
        cannon_group.update() # Atualiza o que acontece com os canhões
    
    # Checa por game over e restart
    if game_over == True:
        if button.draw() ==  True:
            game_over = False
            score = restart()    

    # Tratamento de eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and voando == False and game_over == False:
            voando = True
            
    pygame.display.update()

pygame.quit()



