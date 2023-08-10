import pygame as pg
import sys
from settings import *
from sprites import *        

# GAME ENGINE
class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.key.set_repeat(500, 100)
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.map = []
        self.load_map()

    def load_map(self):
        f = open("./maps/map.txt", "r")
        for line in f:
            self.map.append(line)
            
    def set_up(self):
        # Initialize all variables and do all the set-up for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        
        # Generating the walls of the map
        for y, tiles in enumerate(self.map):
            for x, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, x, y)
                if tile == 'P':
                    self.player = Player(self, x, y)
                
    def run(self):
        # Game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000  # Time between frames in seconds
            self.events()
            self.update()
            self.draw()
            pg.display.update()

    def quit(self):
        pg.quit()
        sys.exit()
    
    def update(self):
        # Update all of our sprites
        self.all_sprites.update()

    def events(self):
        # Catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)

    def start_screen(self):
        pass

    def show_go_screen(self):
        pass

# RUN THE GAME
game = Game()
# game.start_screen()
game.set_up()
game.run()
# game.show_go_screen()
    
       