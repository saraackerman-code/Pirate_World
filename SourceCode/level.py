from pytmx import load_pygame
import pygame

from player import Player
from sprites import Sprite
from settings import *

class Level:
    def __init__(self, tmx_path):
        self.display_surface = pygame.display.get_surface()
        #Groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites= pygame.sprite.Group()

        self.setup(tmx_path)

    def setup(self, tmx_path):
        tmx_data = load_pygame(tmx_path)
        terrain_layer = tmx_data.get_layer_by_name("Terrain")
        for x,y, surf in terrain_layer.tiles():
            Sprite ((x*TITLE_SIZE,y*TITLE_SIZE), surf, (self.all_sprites, self.collision_sprites))
        for obj in tmx_data.get_layer_by_name("Objects"):
            if obj.name == 'player':
                Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)




    def run(self, dt):
        self.all_sprites.update(dt)
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)


