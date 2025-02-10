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
        # Variables
        self.SCREEN_HEIGHT = 1024
        self.SCREEN_WIDTH = 768
        self.CELL_SIZE = 40
        self.ROWS = self.SCREEN_HEIGHT // self.CELL_SIZE
        self.COLS = self.SCREEN_WIDTH // self.CELL_SIZE
        #Init
        pygame.init()
        pygame.display.set_caption("Top Down View Game")

        self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        self.clock = pygame.time.Clock()
        
    def draw_grid(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                rect = pygame.Rect(col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                pygame.draw.rect(self.screen, (0, 0 ,0), rect, 1)
    
    def run(self):
        while True:
            # Quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Wipe last frame
            self.screen.fill("white")
            
            self.draw_grid()
            
            # Draw circles
            for circle in circles:
                circle.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        
Game().run()