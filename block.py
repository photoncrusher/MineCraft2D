import pygame
from src import constants as const
from src import prepare

class Block:
    def __init__(self) -> None:
        self.block_size = const.BLOCK_SIZE
        self.landscape_asset = prepare.GRASS_BLOCK_IMG
        self.dirt_asset = prepare.DIRT_BLOCK_IMG

    # DEF TO GET THE BLOCK STYLE LIKE COLOR, etc...
    def get_block_style(self, block_type):
        if block_type == 'LANDSCAPE':
            self.asset = self.landscape_asset
        if block_type == 'DIRT':
            self.asset = self.dirt_asset

    # VE CAC BLOCK SAU KHI DA TINH TIEN NGANG/ DOC MOT DOAN X,Y. TRONG DO X,Y TINH THEO ORIGINAL
    def get_block_rect(self, block_num1, block_num2, screen_x, screen_y):
        x = self.block_size * block_num1 + screen_x
        y = self.block_size * block_num2 + screen_y
        x = x + 10
        y = y + 10
        return x, y

    # DEF TO DRAW THE BLOCK FROM SCREEN X, Y VALUES
    def draw(self, DISPLAYSURF, heigth_block, width_block, block_type, screen_x, screen_y):
        self.get_block_style(block_type)
        rect = self.asset.get_rect()
        rect.center = self.get_block_rect(heigth_block, width_block, screen_x, screen_y)
        DISPLAYSURF.blit(self.asset, rect)