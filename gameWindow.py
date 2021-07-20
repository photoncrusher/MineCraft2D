import pygame

class gameWindow:
    def __init__(self, width, height) -> None:
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def render(self):     
        self.clock.tick(60)
        return self.screen
        
