import pygame
from pygame.sprite import AbstractGroup

class Block(pygame.sprite.Sprite):

    def __init__(self,  *groups: AbstractGroup):
       super().__init__(*groups)
       self.image = pygame.Surface([50, 50])
       self.image.fill((225,0,0))
       self.rect = self.image.get_rect()
       
    def set_pos(self, i, j):
        self.rect.center = (i,j)