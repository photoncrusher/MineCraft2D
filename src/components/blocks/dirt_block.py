from pygame.sprite import AbstractGroup

from .block import Block
from src import prepare


class DirtBlock(Block):
    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = prepare.DIRT_BLOCK_IMG
        self.rect = self.image.get_rect()
