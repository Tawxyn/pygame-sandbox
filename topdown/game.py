import pygame
import sys
from game_objects import Circle

circles = [
    Circle(pos=(100, 100), radius=50, color=(255, 0, 0)),
    Circle(pos=(200, 200), radius=30, color=(0, 255, 0)),
    Circle(pos=(300, 300), radius=40, color=(0, 0, 255))
    ]

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Top Down View Game")
        
        self.screen = pygame.display.set_mode(rect.size)
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            # Quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Wipe last frame
            self.screen.fill("black")
            
            # Draw circles
            for circle in circles:
                circle.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
Game().run()