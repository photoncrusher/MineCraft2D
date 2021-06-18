import sys
import pygame
from .screen import Screen
from pygame.locals import *
import pygame_gui
import src.constants as const
from src.ui import Button, Label, TextBox
from src.ui.manager import Manager


class StartOptionScreen(Screen):
    def __init__(self, main):
        super().__init__(main)
        self.bg_surface = pygame.image.load(const.START_OPTION_BG_IMG).convert()

        self.manager = Manager((const.WIDTH, const.HEIGTH))
        self.create_ui(self.manager)

    def start_btn_onclick(self):
        self.main.screen = self.main.IN_GAME_SCREEN


    def create_ui(self, manager):
        rect = Rect(0, 0, 120, 40)
        rect.midleft = (const.WIDTH / 8, const.HEIGTH / 10)
        Label(rect, "Player name", manager)

        rect = Rect(0, 0, 200, 40)
        rect.midleft = (const.WIDTH / 8 * 3, const.HEIGTH / 10)
        TextBox(rect, manager, init_text="DRANHCLUB")

        rect = Rect(0, 0, 120, 40)
        rect.midleft = (const.WIDTH / 8, const.HEIGTH / 10 * 2)
        Label(rect, "Seed:", manager)

        rect = Rect(0, 0, 200, 40)
        rect.midleft = (const.WIDTH / 8 * 3, const.HEIGTH / 10 * 2)
        self.seed_textbox = TextBox(rect, manager, init_text="12345")

        rect = Rect(0, 0, 100, 40)
        rect.midleft = (const.WIDTH / 8 * 3, const.HEIGTH / 10 * 3)
        Button(rect, "START", manager)

    def show(self):
        window = self.main.window

        while True:
            window.blit(self.bg_surface, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == USEREVENT:
                    self.main.screen = self.main.IN_GAME_SCREEN
                    self.main.seed = self.seed_textbox.text
                    return
                self.manager.process_event(event)

            self.manager.draw_ui(window)
            pygame.display.update()
