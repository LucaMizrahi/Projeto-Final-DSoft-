from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'Assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'Assets', 'audios')
FNT_DIR = path.join(path.dirname(__file__), 'Assets', 'fontes')

# Dados gerais do jogo.
WIDTH = 1024 # Largura da tela
HEIGHT = 768 # Altura da tela
FPS = 630 # Frames por segundo

# Define tamanhos
PIRATE_WIDTH = int(HEIGHT / 2)
PIRATE_HEIGHT = 200
CANNON_WIDTH = 620
CANNON_HEIGHT = 800

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

