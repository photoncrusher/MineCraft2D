import pygame
from src.constants import *
import pygame
from engine import *
class Player:
    def __init__(self) -> None:
        self.block_size = 20
        self.pos_x = 100
        self.pos_y = 100
        # self.block_color = (26, 176, 36)
    def player_style(self):
        player_color = (26, 176, 36)
        return player_color