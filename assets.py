import pygame
import os
from configuracoes import *

 
BACKGROUND = 'background'
CANNON = 'cannon'
PIRATE = 'pirate'
BUTTON = 'button'
GETREADY = 'get_ready'
SCORE_FONT = 'score_font'
CRASH_SOUND = 'crash_sound'
POINT_SOUND = 'point_sound'
SCORE_FONT = 'score_font'
TELAGAMEOVER = 'tela_gameover'
FIRSTSCREEN = 'First_screen'



def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'padrao_pirata.png')).convert()   
    assets[BACKGROUND] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
    assets[CANNON] = pygame.image.load(os.path.join(IMG_DIR, 'cano1.png')).convert_alpha()
    assets[PIRATE] = pygame.image.load(os.path.join(IMG_DIR, 'Drunken_Sailor.png')).convert_alpha()
    assets[PIRATE] = pygame.transform.scale(assets['pirate'], (70, 70))
    assets[BUTTON] = pygame.image.load(os.path.join(IMG_DIR, 'button.png')).convert()
    assets[GETREADY] = pygame.image.load(os.path.join(IMG_DIR, 'getready.png')).convert_alpha()
    assets[GETREADY] = pygame.transform.scale(assets['get_ready'], (184, 267))
    assets[TELAGAMEOVER] = pygame.image.load(os.path.join(IMG_DIR, 'telagameover.png')).convert()
    assets[TELAGAMEOVER] = pygame.transform.scale(assets['tela_gameover'], (WIDTH, HEIGHT))
    assets[FIRSTSCREEN] = pygame.image.load(os.path.join(IMG_DIR), 'First_screen.png').convert_alpha()
    assets[FIRSTSCREEN] = pygame.transform.scale(assets['First_screen'], (WIDTH, HEIGHT))
    

    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, 'theme.wav'))
    pygame.mixer.music.set_volume(0.4)
    assets[CRASH_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'crash.wav'))
    assets[POINT_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'point.wav'))
    
    # Carrega fonte
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    return assets