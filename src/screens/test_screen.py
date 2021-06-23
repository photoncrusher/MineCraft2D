import pygame
from pygame.locals import *
import sys
from .screen import Screen
import src.constants as const
from src import state, prepare
from src.components.blocks.dirt_block import DirtBlock
from pygame.sprite import Group
from src.components.player import Player


class TestScreen(Screen):
    def __init__(self):
        pass

    def show(self):
        clock = pygame.time.Clock()
        window = state.window
        dirt_group = Group()
        for i in range(0, 20):
            for j in range(20, 25):
                dirt_block = DirtBlock()
                dirt_block.set_pos(i, j)
                dirt_group.add(dirt_block)

        player = Player()
        player_group = Group(player)

        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                player.process_event(event)

            window.fill((255, 255, 255))
            dirt_group.draw(window)
            player_group.draw(window)
            player_group.update()
            pygame.display.update()
