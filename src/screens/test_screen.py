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
        self.font = pygame.font.Font(const.FONT, 20)

    def show(self):
        clock = pygame.time.Clock()
        window = state.window

        # Create dummy terrain
        dirt_group = Group()
        for i in range(0, 500):
            for j in range(20, 25):
                dirt_block = DirtBlock()
                dirt_block.set_pos(i, j)
                dirt_group.add(dirt_block)
        dirt_block = DirtBlock()
        dirt_block.set_pos(15, 19)
        dirt_group.add(dirt_block)

        # Create player
        player = Player()
        player_group = Group([player])

        # A group hold all sprite for drawing with camera
        all_sprites = Group(*dirt_group, *player_group)

        while True:
            # Limit FPS
            clock.tick(60)

            # Process events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                player.process_event(event)
            player_group.update(dirt_group)

            # Draw sprites
            camera_x = player.pos_x - const.WIDTH / 2
            camera_y = player.pos_y - const.HEIGHT / 2
            window.fill((255, 255, 255))
            for sprite in all_sprites:
                window.blit(sprite.image, (sprite.rect.x - camera_x, sprite.rect.y - camera_y))
                
            # draw info
            window.blit(self.font.render(f"{player.key_stack=}", True, (0, 0, 0)), (0, 0))
            window.blit(self.font.render(f"{player.state=}", True, (0, 0, 0)), (0, 20))
            window.blit(self.font.render(f"{player.dir=}", True, (0, 0, 0)), (0, 40))
            window.blit(self.font.render(f"{player.standing=}", True, (0, 0, 0)), (0, 60))

            pygame.display.update()
