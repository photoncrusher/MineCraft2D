from pygame.sprite import AbstractGroup
import pygame
from .block import Block


class DirtBlock(Block):
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface([50, 50])
        self.image.fill((225,225,0))
        self.rect = self.image.get_rect()
