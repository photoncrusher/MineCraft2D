import pygame
from pygame.locals import *
import sys
from .screen import Screen
import src.constants as const
from src import state, prepare


class SplashScreen(Screen):
    def __init__(self):
        pass

    def show(self):
        window = state.window

        # Credit image
        credit = prepare.CREDIT_IMG
        credit = pygame.transform.scale(credit, (const.WIDTH, const.HEIGHT))

        # Get time for delay
        start_time = pygame.time.get_ticks()
        delay = 50  # milliseconds
        index = 0
        while True:
            # Delay
            if pygame.time.get_ticks() - start_time > delay:
                state.screen = const.MAIN_MENU_SCREEN
                return

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            window.fill((0, 255, 0))
            window.blit(credit, (0, 0))
            pygame.display.update()
