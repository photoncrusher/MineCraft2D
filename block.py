import pygame
from src.constants import *
import pygame
class Block:
    def __init__(self) -> None:
        self.block_size = 20
        # self.block_color = (26, 176, 36)
    def get_block_style(self,block_type):
        if block_type == 'GRASS':
            block_color = (26, 176, 36)
            return block_color
        if block_type == 'DIRT':
            block_color = (115, 105, 93)
            return block_color
        if block_type == 'PLAYER':
            block_color = (0, 0, 0)
            return block_color
    def get_block_rect(self,block_num1,block_num2,x,y):
        x = self.block_size * block_num1 + x
        y = self.block_size * block_num2 + y
        return (x,y,self.block_size,self.block_size)
    def draw(self,DISPLAYSURF,heigth_block,width_block,block_type,x,y):
        pygame.draw.rect(DISPLAYSURF,self.get_block_style(block_type),self.get_block_rect(heigth_block,width_block,x,y))