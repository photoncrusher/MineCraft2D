import sys
import pygame
from pygame.locals import *
import src.constants as const
from src.ui import Button, Label, TextBox, ListSelection, ListItem
from src.ui.manager import Manager
from src import state


class SelectWorldScreen():
    def __init__(self):
        self.bg_surface = pygame.image.load(const.START_OPTION_BG_IMG).convert()

    def create_ui(self):
        self.manager = Manager((const.WIDTH, const.HEIGTH))

        # List world
        rect = Rect(0, 80, const.WIDTH, const.HEIGTH - 200)
        self.world_list_selection = ListSelection(rect, self.manager, const.BLACK)

        world_item_1 = ListItem((200, 80), "world 1", self.manager)
        world_item_2 = ListItem((200, 80), "world 2", self.manager)
        world_item_3 = ListItem((200, 80), "world 3", self.manager)
        world_item_4 = ListItem((200, 80), "world 4", self.manager)
        self.world_list_selection.add_items(world_item_1, world_item_2, world_item_3, world_item_4)

        gap = 10

        # "Play selected world" button
        rect = Rect(0, 0, 250, 40)
        rect.topright = ((const.WIDTH / 2 - gap, const.HEIGTH / 16 * 13))
        self.play_btn = Button(rect, "Play selected world", self.manager)

        # Create new world button
        rect = Rect(0, 0, 250, 40)
        rect.topleft = ((const.WIDTH / 2 + gap, const.HEIGTH / 16 * 13))
        self.create_new_world_btn = Button(rect, "Create New World", self.manager)

        # Edit button
        rect = Rect(0, 0, 120, 40)
        rect.topleft = self.play_btn.rect.bottomleft
        rect.move_ip(0, gap)
        self.edit_button = Button(rect, "Edit", self.manager)

        # Delete button
        rect = Rect(0, 0, 120, 40)
        rect.topright = self.play_btn.rect.bottomright
        rect.move_ip(0, gap)
        self.delete_btn = Button(rect, "Delete", self.manager)

        # Cancel button
        rect = Rect(0, 0, 120, 40)
        rect.topright = self.create_new_world_btn.rect.bottomright
        rect.move_ip(0, gap)
        self.cancel_btn = Button(rect, "Cancel", self.manager)

        # Re-create button
        rect = Rect(0, 0, 120, 40)
        rect.topleft = self.create_new_world_btn.rect.bottomleft
        rect.move_ip(0, gap)
        self.re_create_btn = Button(rect, "Re-create", self.manager)

    def show(self):
        window = state.window
        self.create_ui()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == USEREVENT:
                    if event.user_type == const.UI_BUTTON_PRESS:
                        if event.ui_element == self.cancel_btn:
                            state.screen = const.MAIN_MENU_SCREEN
                            return
                        if event.ui_element == self.play_btn:
                            state.screen = const.IN_GAME_SCREEN
                            return
                self.manager.process_event(event)

            window.blit(self.bg_surface, (0, 0))
            self.manager.draw_ui(window)
            pygame.display.update()
