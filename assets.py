import pygame
import os
from configuracoes import *


BACKGROUND = 'padrao_pirata'
CANNON_IMG = 'Cannon_img'
CANNON_IMG = 'Cannon_img'
PIRATE_IMG = 'Drunken Sailor_img'
PIRATE_IMG = 'Drunkeb Sailor_img'
SCORE_FONT = 'score_font'
CRASH_SOUND = 'crash_sound'
POINT_SOUND = 'point_sound'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'padrao_pirata.png')).convert()
    assets[CANNON_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Cannon.png')).convert_alpha()
    assets[CANNON_IMG] = pygame.transform.scale(assets['Cannon_img'], (CANNON_WIDTH, CANNON_HEIGHT))
    assets[PIRATE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Drunken Sailor.png')).convert_alpha()
    assets[PIRATE_IMG] = pygame.transform.scale(assets['Pirate_img'], (PIRATE_WIDTH, PIRATE_HEIGHT))

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'theme.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[CRASH_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'crash.wav'))
    assets[POINT_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'point.wav'))
    return assets