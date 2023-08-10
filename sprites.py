import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites
        super().__init__(self.groups)
        
        self.create_sprite()
        self.x = x * TILESIZE
        self.y = y * TILESIZE
    
    def create_sprite(self):
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()

    def update(self):
        """
        Updates the player's location according to tile coordinates.
        All interactive sprites must have an update method.
        Called in game's update method.
        """
        self.key_pressed()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt

        self.rect.x = self.x
        self.rect.y = self.y

    def key_pressed(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN]:
            self.vy = PLAYER_SPEED

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # Adding into all_sprites group
        self.groups = game.all_sprites, game.walls
        super().__init__(self.groups)   
        
        # Bring up Game obj
        self.game = game
        
        # Setting up image and rect
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        
        # Wall position
        self.x = x
        self.y = y
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE