from pygame.sprite import Sprite, AbstractGroup
from src import prepare
import src.constants as const


class Block(Sprite):
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)

    def set_pos(self, i, j):
        self.rect.center = (i * const.BLOCK_SIZE, j * const.BLOCK_SIZE)
