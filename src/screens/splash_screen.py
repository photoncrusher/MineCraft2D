import pygame
from pygame.locals import *
import sys
from .screen import Screen
import src.constants as const


class SplashScreen(Screen):
    def __init__(self, main):
        super().__init__(main)

    def show(self):
        window = self.main.window

        credit = pygame.image.load(const.CREDIT_IMG)
        credit.convert()
        credit = pygame.transform.scale(credit, (const.WIDTH, const.HEIGTH))

        start_time = pygame.time.get_ticks()
        delay = 500  # milliseconds

        while True:
            if pygame.time.get_ticks() - start_time > delay:
                self.main.screen = self.main.MAIN_MENU_SCREEN
                return

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            window.fill(const.BACKGROUND_COLOR)
            window.blit(credit, (0, 0))
            pygame.display.update()
