import random
import pygame
from configuracoes import WIDTH, HEIGHT, CANNON_WIDTH, CANNON_HEIGHT, PIRATE_WIDTH, PIRATE_HEIGHT
from assets import PIRATE_IMG, CANNON_IMG


class pirate(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/img/Drunken_Sailor.png').convert_alpha()
        # self.image = pygame.transform.scale(self.image, (110,110))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.pulo = False

    def update(self):
        #Gravidade
        self.vel += 0.5
        if self.vel>8:
            self.vel = 8
        if self.rect.bottom<HEIGHT :
            self.rect.y += int(self.vel)

        #Pulo
        if pygame.K_SPACE.get_pressed()[0] == 1 and self.pulo == False:
            self.pulo = True
            self.vel = -10
        if pygame.K_SPACE.get_pressed()[0] == 0 and self.pulo == False:
            self.pulo = False

        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    
class cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/img/Cannon.png').convert_alpha()
        #self.image = pygame.transform.scale(self.image, (110,110))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if posicao == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.up = [x, y + int(400/2)]
        if posicao == -1:
            self.rect.down = [x, y + int(400/2)]

    def update(self):
        self.rect.x -= 4

sailor_group = pygame.sprite.Group()
cannon_group = pygame.sprite.Group()

p = pirate(200, int(HEIGHT / 2))
c1 = cannon(800, 628, -1)
c2 = cannon(800, int(HEIGHT/2), 1)

sailor_group.add(p)
cannon_group.add(c1)
cannon_group.add(c2)