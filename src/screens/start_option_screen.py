import sys
import pygame
from .screen import Screen
from pygame.locals import *
import pygame_gui
import src.constants as const
from src.ui import Button, Label, TextBox
from src.ui.manager import Manager
from src import state


class StartOptionScreen(Screen):
    def __init__(self):
        self.bg_surface = pygame.image.load(const.START_OPTION_BG_IMG).convert()
        self.create_ui()

    def create_ui(self):
        self.manager = manager = Manager((const.WIDTH, const.HEIGHT))

        rect = Rect(0, 0, 120, 40)
        rect.midleft = (const.WIDTH / 8, const.HEIGHT / 10)
        Label("Player name", manager)

        rect = Rect(0, 0, 200, 40)
        rect.midleft = (const.WIDTH / 8 * 3, const.HEIGHT / 10)
        TextBox(rect, manager, init_text="DRANHCLUB")

        rect = Rect(0, 0, 120, 40)
        rect.midleft = (const.WIDTH / 8, const.HEIGHT / 10 * 2)
        Label("Seed:", manager)

        rect = Rect(0, 0, 200, 40)
        rect.midleft = (const.WIDTH / 8 * 3, const.HEIGHT / 10 * 2)
        self.seed_textbox = TextBox(rect, manager, init_text="12345")

        rect = Rect(0, 0, 100, 40)
        rect.midleft = (const.WIDTH / 8 * 3, const.HEIGHT / 10 * 3)
        self.start_btn = Button(rect, "START", manager)

    def show(self):
        window = state.window

        while True:
            window.blit(self.bg_surface, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == USEREVENT:
                    if event.user_type == const.UI_BUTTON_PRESS:
                        if event.ui_element == self.start_btn:
                            state.screen = const.IN_GAME_SCREEN
                            state.seed = self.seed_textbox.text
                            return

                self.manager.process_event(event)

            self.manager.draw_ui(window)
            pygame.display.update()
