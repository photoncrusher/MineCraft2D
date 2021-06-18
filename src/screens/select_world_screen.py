import sys
import pygame
from .screen import Screen
from pygame.locals import *
import src.constants as const
from src.ui import Button, Label, TextBox, ListSelection, ListItem
from src.ui.manager import Manager


class SelectWorldScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.bg_surface = pygame.image.load(const.START_OPTION_BG_IMG).convert()

    def create_ui(self):
        self.manager = Manager((const.WIDTH, const.HEIGTH))

        rect = Rect(0, 80, const.WIDTH, const.HEIGTH - 120)
        self.world_list_selection = ListSelection(rect, self.manager, const.BLACK)

        world_item_1 = ListItem(Rect(0, 0, 200, 80), "world 1", self.manager)
        world_item_2 = ListItem(Rect(0, 0, 200, 80), "world 2", self.manager)
        world_item_3 = ListItem(Rect(0, 0, 200, 80), "world 3", self.manager)
        world_item_4 = ListItem(Rect(0, 0, 200, 80), "world 4", self.manager)
        self.world_list_selection.add_items(world_item_1, world_item_2, world_item_3, world_item_4)

    def show(self):
        window = self.main.window
        self.create_ui()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                self.manager.process_event(event)

            window.blit(self.bg_surface, (0, 0))
            self.manager.draw_ui(window)
            pygame.display.update()
