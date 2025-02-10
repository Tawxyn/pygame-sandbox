import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        pass
    
    def run(self):
        while True:
            # Quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
Game().run()