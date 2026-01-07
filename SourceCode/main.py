import pygame

from settings import *
from level import Level
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Super Pirate World")
        self.clock = pygame.time.Clock()

        self.tmx_path = r"S:\Game_project\Super-Pirate-World-main\Super-Pirate-World-main\data\levels\omni.tmx"
        self.current_stage = Level(self.tmx_path)

    def run(self):
        while True:
            dt = self.clock.tick()/ 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()
if __name__ == "__main__":
    game = Game()
    game.run()
    import os


