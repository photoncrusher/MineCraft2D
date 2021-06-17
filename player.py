import pygame
from src.constants import *
import pygame
from engine import *
from src.animate import *
class Player:
    def __init__(self) -> None:
        self.pos_x = 1000
        self.pos_y = 0
        self.image = get_a(PLAYER_IMG, 75,80)
        self.block_size = 20
    def player_style(self):
        player_color = (26, 176, 36)
        return player_color

    def get_block_rect(self, block_num1, block_num2, screen_x, screen_y):
        x = self.block_size * block_num1 + screen_x
        y = self.block_size * block_num2 + screen_y
        return x, y

    def draw(self, DISPLAYSURF, heigth_block, width_block, screen_x, screen_y, index):
        rect = self.image[int(index)].get_rect()
        rect.center = self.get_block_rect(heigth_block,width_block,screen_x,screen_y)
        DISPLAYSURF.blit(self.image[int(index)], rect)
