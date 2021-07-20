import pygame
from pygame.rect import Rect
from pygame.sprite import AbstractGroup
from .animate import get_a
import math
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface([50,70], flags=pygame.SRCALPHA)
        self.image1 = get_a("E:\\Working place\\NEW20202\\mc2d-game\\Curved\\image\\minecraft_player.gif", 50,70)
        self.image.blit(self.image1[0], (0,0), Rect(0,0,50,70))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
    def update(self, collide_group, **kwargs):
        collider = pygame.sprite.spritecollide(self, collide_group, False)
        data = []
        if collider:
            for col in collider:
                x2 = col.rect.centerx
                y2 = col.rect.centery
                x1 = self.rect.centerx
                y1 = self.rect.centery
                if x2-x1 == 0 or abs(y2-y1) / abs(x2-x1) > (self.rect.height/2) / 25:
                    if y2 > y1:
                        data.append('DOWN')
                    if y2 < y1:
                        data.append('UP')
                elif x2-x1 != 0 and abs(y2-y1) / abs(x2-x1) < (self.rect.height/2) / 25 - 1:
                    if x2 > x1:
                        data.append('RIGHT')
                    if x2 < x1:
                        data.append('LEFT')
        return data
    

    
