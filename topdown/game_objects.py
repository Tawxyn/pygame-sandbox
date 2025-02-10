import pygame

class Circle:
    
    def __init__(self, pos, radius, color):
        self.pos = pos
        self.radius = radius
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos), self.radius)
        