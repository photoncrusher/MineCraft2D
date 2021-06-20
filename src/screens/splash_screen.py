import pygame
from pygame.locals import *
import sys
from .screen import Screen
import src.constants as const
from src import state


class SplashScreen(Screen):
    def show(self):
        window = state.window

        credit = pygame.image.load(const.CREDIT_IMG)
        credit.convert()
        credit = pygame.transform.scale(credit, (const.WIDTH, const.HEIGHT))

        start_time = pygame.time.get_ticks()
        delay = 50  # milliseconds

        while True:
            if pygame.time.get_ticks() - start_time > delay:
                state.screen = const.MAIN_MENU_SCREEN
                return

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            window.fill(const.WHITE)
            window.blit(credit, (0, 0))
            pygame.display.update()
