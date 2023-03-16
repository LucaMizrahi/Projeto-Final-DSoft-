#Imports
import pygame
from assets import PIRATE,CANNON, BUTTON

#Função declara a mascara dos sprites que interagem entre si
def mascara(x,assets,asset):
    x.image = assets[asset]
    x.mask = pygame.mask.from_surface(x.image)
    x.rect = x.image.get_rect()
    return x.image,x.mask, x.rect

#Classe Pirata
class pirate(pygame.sprite.Sprite):
    def __init__(self, x, y,assets):
        pygame.sprite.Sprite.__init__(self)
        mascara(self,assets,PIRATE)
        self.rect.center = [x, y]
        self.vel = 0
        self.click = False
    
    def update(self,voando,game_over):
        
        # Gravidade
        if voando == True:
            self.vel += 0.5
            self.vel = min(self.vel, 8)
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over == False:
            # Pulo 
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False

#Classe Canhao
class cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, posicao,assets):
        pygame.sprite.Sprite.__init__(self)
        mascara(self,assets,CANNON)

        # A posição 1 equivale ao cano vindo de cima e -1 ao cano vindo de baixo
        if posicao == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y]
        if posicao == -1:
            self.rect.topleft = [x, y]
    
    def update(self,vel_fundo):
        self.rect.x -= vel_fundo

        # Tira os canhões que já passaram pela tela
        if self.rect.right < 0:
            self.kill()

#Classe Botao
class Button():
        def __init__(self, x, y,assets):
            mascara(self,assets,BUTTON)
            self.rect.topleft = (x, y)

        def draw(self,window):
            # Ver a posição do mouse
            posicao = pygame.mouse.get_pos()

            action = bool(
                self.rect.collidepoint(posicao) and pygame.mouse.get_pressed()[0] == 1
            )
            # Desenha botão
            window.blit(self.image, (self.rect.x, self.rect.y))
            return action