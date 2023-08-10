import pygame as pg

# Standard colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 254)

# Game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BLACK

# Tiles
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Font
# FONT = pg.font.SysFont("Verdana", 60) # change font
# SMALLFONT = pg.font.SysFont("Verdana", 20) # change font
# GAMEOVER = FONT.render("Game Over", True, BLACK) 

# Player settings
PLAYER_SPEED = 100